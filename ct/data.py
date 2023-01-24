from pathlib import Path
from unidecode import unidecode
import string

class StopWords:
    def __init__(self, path: Path = Path('stopwords.txt')):
        self.path = path
        self._read()

    def _read(self):
        stopwords = self.path.read_text()
        stopwords = stopwords.split('\n')
        stopwords.extend([w.upper() for w in stopwords])
        self.stopwords = stopwords

class Data:
    def __init__(self, data_path: Path, stopwords: StopWords) -> None:
        self.stopwords = stopwords
        if data_path.is_dir():
            self.path = [p for p in data_path.glob('*.txt')]
        else:
            self.path = [data_path]

        self.data = self._read()
        self.clean_data = self._clean()
    
    @staticmethod
    def strip_punctuation(text):
        return ''.join([t for t in text if not t in string.punctuation])

    def strip_stopwords(self, text):
        output = []
        for t in text.split(' '):
            if t not in self.stopwords.stopwords:
                output.append(t)
                output.append(' ')
        return ''.join(output)

    def _read(self) -> None:
        data = []
        for path in self.path:
            data.extend(path.read_text().split('\n'))
        return [d.strip() for d in data]

    def _clean(self) -> None:
        return [self.clean_text(text) for text in self.data]

    def clean_text(self, text: str) -> str:
        return unidecode(self.strip_punctuation(self.strip_stopwords(text))).lower().strip()

    def to_string(self, clean = True):
        if clean:
            return '\n'.join(self.clean_data)
        return '\n'.join(self.data)

    def save(self, path, clean: bool) -> None:
        path.write_text(self.to_string(clean))
            
    