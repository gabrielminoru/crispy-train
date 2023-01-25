from ct.data import StopWords, Data
from ct.gpt3 import Chat
from ct.searcher import DumbSearcher
from pathlib import Path
from config import settings

# getting data
stopwords = StopWords(Path('stopwords.txt'))
data = Data(Path('data/data.txt'), stopwords)

# setting up searcher, will use only 15 paragraphs
searcher = DumbSearcher(data, limiter = 3)

# initializing chat
chat = Chat(settings, botname = "o tal do sheepz")
chat.set_searcher(searcher = searcher)

if __name__ == "__main__":
    chat.run()
        

