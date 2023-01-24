import openai
from pathlib import Path
import string
from unidecode import unidecode
from config import settings
from ct.prompt import Searcher, Prompt
from ct.data import Data

#openai.api_key=settings.openai_token

class Chat:
    def __init__(self, settings, botname):
        openai.api_key = settings.openai_token
        self.name = botname

    def setup(self, searcher):
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
        while True:
            raw = input("Você: ")
            print('\n')
            print(f"{self.name}: {self.msg(Prompt(raw, self.searcher).enhance())}")
            print('\n')
