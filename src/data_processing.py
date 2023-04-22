import pandas as pd 
import spacy
import string
from spacy.lang.en import English
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')

putback = ['prime', 'officials', 'security', 'news', 'working', 'games', 'jobs', 'campaign', 'services',
'civil', 'economic', 'information', 'political', 'election', 'court', 'office', 'vote', 'trump', 'control', 'job', 'price',
'donald trump', 'chinese', 'problems', 'concerns', 'minister', 'nation', 'policy', 'data', 'indian', 'congress',
'president', 'network', 'american', 'accused', 'government', 'money', 'investigation', 'facebook', 
'success', 'prices', 'twitter', 'book', 'politics',  'justice', 'claims', 'russia', 'law', 'technology',
'content', 'union', 'european', 'workers']

def construct_list_stopwords(list_putback_words=putback):
  '''
  On importe la liste des stopwords :
  On a donc un dataframe des stopwords. On en tire une liste simple des stopwords, où l'on remet cependant des stopwords jugés significatifs, comme expliqué pour le traitement des journaux :
  
  Parameters:
  -----------
  list_putback_words : list des mot jugés finalement signifcatifs 
  '''
  df_stopwords = pd.read_csv("00. input/sw1k.csv",
                names=['word', 'frequency', 'presence', 'doc_size_sum', 'type'],
                encoding='latin-1').drop(index=0)
  stopwords = df_stopwords['word'].unique()
  stopwords = list(set(stopwords) - set(list_putback_words))
  stopwords += ['hon']
  return stopwords

nlp = spacy.load('en_core_web_sm')
nlp.disable_pipes(["tagger", "parser"])
stemmer = SnowballStemmer(language='english')

english_stopwords = set(stopwords.words('english'))

def extract_bigrams(n_grams):
  bigrams = []
  for i in range(len(n_grams)-1):
    bigram = f'{n_grams[i]} {n_grams[i+1]}'
    bigrams.append(bigram)
  return bigrams

def clean(text: str, gram:str):
  '''
  On va cleen le text
  On utilise la librairie SpaCy comme pour le traitement des journaux, et on enlève les nombres et la ponctuation avec la méthode translate. 
  
  Parameters:
  -----------
  text : le texte sur lequel on fait le processing
  '''
  text = str(text).lower()
  text = text.translate(str.maketrans('', '', string.punctuation))
  text = text.translate(str.maketrans('', '', string.digits)) 
  # tokenization
  tokens = word_tokenize(text)
  # Enlever les caractères qui ne sont pas des lettres
  tokens = [re.sub('[^a-zA-Z]', '', token) for token in tokens]
  # Stemming
  stemmer = PorterStemmer()
  tokens_stemmed = [stemmer.stem(token) for token in tokens]
  filtered_words = [word for word in tokens_stemmed if not word.lower() in english_stopwords]
  if (gram == 'bigram'):
    filtered_words = extract_bigrams(filtered_words)
  return filtered_words

def process_list_BigTech_words(topics: list):
  '''
  Obtient une liste cleen des topics BigTech traités

  Parameters:
  -----------
  topics : liste des topics de la bigTech 
  '''
  string_of_topics = ' '.join(topics)
  string_of_topics = stemmer.stem(string_of_topics)
  list_stem_topics = string_of_topics.split(' ')
  return list_stem_topics

def lines_to_keep(titre: str, liste_big_tech: list):
  '''
  prend en input le titre du speech
  retourne un booleen qui indique si le speech est en lien avec le domaine de la big tech

  Parameters:
  -----------
  titre : titre du speech étudié
  liste_big_tech : set des mots en lien avec la BigTech
  '''
  if len(set(titre) & liste_big_tech) > 0:
      return True
  return False

def keep_Bigtech_speeches(df: pd.DataFrame, list_stem_topics: list):
  '''
  prend en input le DataFrame des inputs 
  renvoie le df contenant uniquement les lignes contenant des speechs en lien avec la BigTech

  Parameters:
  -----------
  df : Dataframe des inputs
  list_stem_topics : liste des mots en lien avec la BigTech
  '''
  set_stem_topics = set(list_stem_topics)
  df['lines_to_keep'] = df['agenda'].apply(lines_to_keep, args=(set_stem_topics,))
  df = df.loc[df['lines_to_keep']]
  df.drop(columns=['agenda', 'lines_to_keep'], inplace=True)
  return df 

def count_freqs(df: pd.DataFrame, party: str):
  '''
  prend en input le DataFrame
  renvoie le df des fréquences pour un parti donné

  Parameters:
  -----------
  df : le Dataframe 
  party : le parti politique pour lequel on souhaite les freqs 
  '''  
  aux = df[['party', 'text']] 
  list_of_words = pd.Series(aux.groupby(by=['party']).sum().loc[party, 'text'])
  freq_df = pd.DataFrame(list_of_words.value_counts(), columns=[f'freq_{party}'])
  freq_df = freq_df.reset_index().rename(columns={'index':"words"})
  return freq_df

def merge_freq(df_1: pd.DataFrame, df_2: pd.DataFrame):
  '''
  permet de faire le merge entre les freq_df des différents partis

  Parameters:
  -----------
  df_1 -> DataFrame : Dataframe 
  df_2 -> DataFrame : Dataframe 
  '''  
  df_freqs = pd.merge(
    df_1,
    df_2,
    how='outer',
    on=['words'],
  )
  return df_freqs


def count_liste(list: list, mot: str):
    '''
    calcule la fréquence de mot dans la list

    Parameters:
    -----------
    list : la liste qu'on étudie 
    mot : le mot dont on veut calculer la fréquence
    '''
    return list.count(mot)

def selected_words(df_freqs):
    return df_freqs['words'].unique()

def construct_df_reg(df: pd.DataFrame, df_freqs: pd.DataFrame, list_of_words: list):
    '''
    Construire le df qui va nous aider à faire nos régressions 

    Parameters:
    -----------
    df_freqs -> DataFrame : le df des freqs
    '''
    for word in list_of_words:
        df[f'{word}'] = df['text'].apply(count_liste, args=(word,))
    return df 

def normalize(df: pd.DataFrame, list_of_words: list):
    '''
    Normaliser les coeffs du Df 

    Parameters:
    -----------
    df -> DataFrame : le df 
    '''
    df['somme'] = df.sum(axis=1)
    df.loc[df['somme'] == 0, 'somme'] = 1
    for word in list_of_words:
        df[f'{word}'] = df[f'{word}'] / df['somme'] 
    return df

def party_str_to_dummy(df: pd.DataFrame):
  df.loc[df['party'] == 'Con', 'party_bool'] = 1
  df.loc[df['party'] == 'Lab', 'party_bool'] = 0
  return df 