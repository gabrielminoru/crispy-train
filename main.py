from ct import data, gpt3, prompt
from pathlib import Path
from config import settings

# getting data
stopwords = data.StopWords(Path('stopwords.txt'))
data = data.Data(Path('data/data.txt'), stopwords)

# setting up searcher, will use only 15 paragraphs
searcher = prompt.Searcher(data, limiter = 15)

# initializing chat
chat = gpt3.Chat(settings, botname = "Barbosa Bot")

chat.setup(searcher = searcher)

if __name__ == "__main__":
    chat.run()

