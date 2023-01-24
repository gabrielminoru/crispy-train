from ct.data import Data

class Searcher:
    def __init__(self, data, limiter = 10):
        self.data = data
        self.limiter = limiter

    def search(self, prompt):
        relevant = []
        for p in prompt:
            for d in self.data.clean_data:
                if p in d:
                    relevant.append(d)

        return relevant[:self.limiter]
 
    

class Prompt:
    def __init__(self, prompt: str, searcher: Searcher):
        self.searcher = searcher
        self.clean_prompt = self.searcher.data.clean_text(prompt)
        self.prompt = prompt

    def _get_relevant(self):
        return self.searcher.search(self.clean_prompt)

    def enhance(self):
        return f"{' '.join(self._get_relevant())} {self.prompt}"
