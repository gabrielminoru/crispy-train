from ct.data import Data
from ct.searcher import Searcher

class Prompt:
    def __init__(self, prompt: str, searcher: Searcher):
        self.searcher = searcher
        self.clean_prompt = self.searcher.data.clean_text(prompt)
        self.prompt = prompt

    def _get_relevant(self):
        return self.searcher.search(self.clean_prompt)

    def enhance(self):
        return f"{' '.join(self._get_relevant())} {self.prompt}"
