import pandas as pd 
import spacy

# j'essaye d'ajouter des trucs pour essayer de commit et de push plus tard 

from spacy.lang.en import English
nlp = spacy.load('en_core_web_sm')
nlp.disable_pipes(["tagger", "parser"])
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')

df_stopwords = pd.read_csv("00. input/sw1k.csv",
                names=['word', 'frequency', 'presence', 'doc_size_sum', 'type'],
                encoding='latin-1').drop(index=0)

stopwords = []
putback = ['prime', 'officials', 'security', 'news', 'working', 'games', 'jobs', 'campaign', 'services',
'civil', 'economic', 'information', 'political', 'election', 'court', 'office', 'vote', 'trump', 'control', 'job', 'price',
'donald trump', 'chinese', 'problems', 'concerns', 'minister', 'nation', 'policy', 'data', 'indian', 'congress',
'president', 'network', 'american', 'accused', 'government', 'money', 'investigation',
'facebook', 'success', 'prices', 'twitter', 'book', 'politics',
'justice', 'claims', 'russia', 'law', 'technology', 'content', 'union', 'european', 'workers']

for i in df_stopwords.index :
  if df_stopwords["word"][i] not in putback :
    stopwords.append(stemmer.stem(df_stopwords["word"][i]))
    stopwords.append('I') # pk tu rajoutes des I à ta liste ?

def clean(text):
  text = str(text).lower()
  text = text.translate(str.maketrans('', '', string.punctuation))
  remove_digits = str.maketrans('', '', string.digits)
  text = text.translate(remove_digits) 
  doc = nlp(text)
  l = []
  for word in doc :
    word = str(word)
    l.append(stemmer.stem(word))
    if l[-1] == ' ' or l[-1] in stopwords: 
      l.pop()
  return l