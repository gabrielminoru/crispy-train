from abc import ABC, abstractmethod


class Searcher(ABC):
    def __init__(self, data, limiter = 10):
        self.data = data
        self.limiter = limiter
        self.clean_prompt_is_set = False

    @abstractmethod
    def search(self, prompt: str) -> list:
        pass

    def set_clean_prompt(self, fn = None):
        if fn:
            self.clean_text = fn
            return
        self.clean_text = self.data.clean_text

    def enhance(self, prompt: str) -> str:
        if not hasattr(self, 'clean_text'):
            self.set_clean_prompt()

        prompt_clean = self.clean_text(prompt)
        return f"{' '.join(self.search(prompt_clean))} {prompt}"

class DumbSearcher(Searcher):
    def search(self, prompt):
        relevant = []
        for p in prompt:
            for d in self.data.clean_data:
                if p in d:
                    relevant.append(d)
        return relevant[:self.limiter]

class w2vSearcher(Searcher):
    def search(self, prompt):
        pass