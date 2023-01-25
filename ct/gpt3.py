import openai
from ct.searcher import DumbSearcher

#openai.api_key=settings.openai_token

class Chat:
    def __init__(self, settings, botname):
        openai.api_key = settings.openai_token
        self.name = botname

    def set_searcher(self, searcher):
        self.searcher = searcher

    def msg(self, prompt):
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

        return response['choices'][0]['text']

    def run(self):
        assert hasattr(self, "searcher"), "Searcher was not set up, use Chat.set_searcher(searcher: Searcher) to set it up."
        while True:
            raw = input("Você: ")
            print('\n')
            print(f"{self.name}: {self.msg(self.searcher.enhance(raw))}")
            print('\n')
