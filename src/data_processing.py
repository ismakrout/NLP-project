import pandas as pd 
import spacy
import string
from spacy.lang.en import English
from nltk.stem.snowball import SnowballStemmer

putback = ['prime', 'officials', 'security', 'news', 'working', 'games', 'jobs', 'campaign', 'services',
'civil', 'economic', 'information', 'political', 'election', 'court', 'office', 'vote', 'trump', 'control', 'job', 'price',
'donald trump', 'chinese', 'problems', 'concerns', 'minister', 'nation', 'policy', 'data', 'indian', 'congress',
'president', 'network', 'american', 'accused', 'government', 'money', 'investigation', 'facebook', 
'success', 'prices', 'twitter', 'book', 'politics',  'justice', 'claims', 'russia', 'law', 'technology',
'content', 'union', 'european', 'workers']

def construct_list_stopwords(list_putback_words=putback):
  '''
  Objectif:
  On importe la liste des stopwords :
  On a donc un dataframe des stopwords. On en tire une liste simple des stopwords, où l'on remet cependant des stopwords jugés significatifs, comme expliqué pour le traitement des journaux :
  
  Arguments:
  list_putback_words -> list des mot jugés finalement signifcatifs 
  '''
  df_stopwords = pd.read_csv("00. input/sw1k.csv",
                names=['word', 'frequency', 'presence', 'doc_size_sum', 'type'],
                encoding='latin-1').drop(index=0)
  stopwords = df_stopwords['word'].unique()
  stopwords = list(set(stopwords) - set(list_putback_words))
  return stopwords

nlp = spacy.load('en_core_web_sm')
nlp.disable_pipes(["tagger", "parser"])
stemmer = SnowballStemmer(language='english')

def clean(text, list_stopwords):
  '''
  Objectif:
  On va cleen le text
  On utilise la librairie SpaCy comme pour le traitement des journaux, et on enlève les nombres et la ponctuation avec la méthode translate. 
  
  Arguments:
  text -> str: le texte sur lequel on fait le processing
  list_stopwords -> list: mots à écarter !
  '''
  text = str(text).lower()
  text = text.translate(str.maketrans('', '', string.punctuation))
  text = text.translate(str.maketrans('', '', string.digits)) 
  doc = nlp(text)
  cleen_text = []
  for word in doc :
    word = str(word)
    cleen_text.append(stemmer.stem(word))
    if (cleen_text[-1] == ' ') or (cleen_text[-1] in list_stopwords): 
      cleen_text.pop()
  return cleen_text

technology=['technology','innovat','computer','high tech|high-tech','science','engineering']
consumer_protection=['privacy','data leak','leak','fake news',' safety','decept','defective','hack']
firms=['google','alphabet','apple','facebook','meta','amazon','microsoft']
products=['chrome','incognito','youtube','nexus','pixel','google drive','gmail','glass','street view','buzz','fitbit',
 'maps', 'doodle','play','translate','search', 'google news','nest hub','xl','nest','chromecast','stadia','hub',
 'marshmallow','lollipop','cloud','waymo','earth','engine',

'apple pay','apple watch','iphone','ipad','ipod','iwatch','macbook','macbook pro', 'macbook air','mac',
 'imac','airpods','ios','siri','icloud','apple tv','apple music','app store', 'safari','x','app','apple store',
 'xr', 'xs', 'se','iphones','itunes','ibook','plus','pro','max','mini','os','airtag','airtags','arcade','homepod',
'keynote','ipados','id','foxconn','facetime','beat','stalk',

'messenger','instagram', 'whatsapp','page','feed','oculus',

'prime', 'kindle',
'publishing','amazon prime','amazon drive','amazon video','amazon business','amazon web service',
'amazon cloud', 'alexa','echo dot','echo','dot', 'delivery', 'amazon uk','unlimited', 'episode','foods','grocery', 
'grand tour','grand','tour','viking', 'vikings','argo','argos','macmillan', 'dvd','clarkson','lord','ring','hair','skin','vacuum',
'pre','beer','drake','spark','kart','dog','twitch','cat','xo','matthew','stafford','ratchet','clank',
'swagway','album','mouse','showbiz','beauty','guardian','batman','arkham','gc','hair','skin','shirt',
'lovefilm','mirzapur','cast','audio','drama','movie','jack ryan','actor','character','lucifer','outlander',
'premier','super mario','sky','channel','voyage',


'windows','window','xp','surface','xbox','studio','microsoft office', 'office','word','cortana', 'surface pro','teams',  'playstation',
'microsoft edge', 'edge', 'gear','outlook','halo','skype','kinect','internet explorer','explorer','ie','bing','xcloud','hololens',
'forza','ori','scarlett','scorpio','wordperfect','valhalla','onedrive','games gold','lumia','azure',
'assassin creed','assassin','creed','minecraft','yammer','warcraft','tay']



ceos=['sundar','pichai','eric','schmidt','steve jobs','tim cook','mark zuckerberg','andy jassy','jeff','bezos','satya', 'nadella','bill gates',
      'gates','steve job','steve','tim', 'cook','zuckerberg','ceo','tim cook ','steve ballmer','ballmer','elop',
      'schiller','fadell','phil spencer','spencer','mcspirit','sandberg','paul','allen','larry hryb','hryb']
      

types=['tablet','mobile', 'laptop', 'pc', 'computer', 'desktop','smartphone', 'smartwatch', 'search engine', 'software','hardware',
               'machine', 'browser','ebook', 'book',  'reader',  'console', 'headphone', 'earbud','bud','store','music',
              'gaming', 'operating','streaming','title','chatbot']



competitor=['samsung', 'galaxy',  'twitter','tiktok', 'switch','sony', 'asos', 'activision blizzard', 'activision','blizzard',
            'nintendo','snes', 'netflix','android','yahoo','nokia','huawei','motorola','htc','blackberry','oppo','oneplus','rim','symbian','bbc','morrison','spotify'] 


configue=['device','feature','battery','screen','sound','gb','g','k','mm','chip','processor','design','display','touch','ram',
          'inch','keyboard','camera','handset','speaker','button','touchscreen','storage', 'data']


celebrity=['dubost','neymar','amanda','beyonce','blur','richard','hammond','ranj','jeremy clarkson', 'jeremy','momoa',
           'jared','aniston','smith','kim','tony','tom','sophie','oasis','trio','sharon','betty','raoul','moat','lauren','andrew',
           'samuel gibbs','samuel','gibbs','van','gaal']

topics = celebrity + configue + competitor + types + ceos + products + firms + consumer_protection + technology

def process_list_BigTech_words(topics):
  '''
  Objectifs:
  Obtient une liste cleen des topics BigTech traités

  Arguments:
  topics -> list : liste des topics de la bigTech 
  '''
  string_of_topics = ' '.join(topics)
  string_of_topics = stemmer.stem(string_of_topics)
  list_stem_topics = string_of_topics.split(' ')
  return list_stem_topics

def lines_to_keep(titre, liste_big_tech):
  '''
  Objectifs:
  prend en input le titre du speech
  retourne un booleen qui indique si le speech est en lien avec le domaine de la big tech

  Arguments:
  titre -> list : titre du speech étudié
  liste_big_tech -> set : set des mots en lien avec la BigTech
  '''
  if len(set(titre) & liste_big_tech) > 0:
      return True
  return False

def keep_Bigtech_speeches(df, list_stem_topics):
  '''
  Objectifs:
  prend en input le DataFrame des inputs 
  renvoie le df contenant uniquement les lignes contenant des speechs en lien avec la BigTech

  Arguments:
  df -> DataFrame : Dataframe des inputs
  list_stem_topics -> list : liste des mots en lien avec la BigTech
  '''
  set_stem_topics = set(list_stem_topics)
  df['lines_to_keep'] = df['agenda'].apply(lines_to_keep, args=(set_stem_topics,))
  df = df.loc[df['lines_to_keep']]
  df.drop(columns=['agenda', 'lines_to_keep'], inplace=True)
  return df 

def count_freqs(df, party):
  '''
  Objectifs:
  prend en input le DataFrame
  renvoie le df des fréquences pour un parti donné

  Arguments:
  df -> DataFrame : Dataframe 
  party -> str : le parti politique pour lequel on souhaite les freqs 
  '''  
  aux = df[['party', 'text']] 
  list_of_words = pd.Series(aux.groupby(by=['party']).sum().loc[party, 'text'])
  freq_df = pd.DataFrame(list_of_words.value_counts(), columns=[f'freq_{party}'])
  freq_df = freq_df.reset_index().rename(columns={'index':"words"})
  return freq_df

def merge_freq(df_1, df_2):
  '''
  Objectifs:
  permet de faire le merge entre les freq_df des différents partis

  Arguments:
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


def count_liste(list, mot):
    '''
    Objectifs:
    calcule la fréquence de mot dans la list

    Arguments:
    list -> list : la liste qu'on étudie 
    mot : le mot dont on veut calculer la fréquence
    '''
    return list.count(mot)

def selected_words(df_freqs):
    return df_freqs['words'].unique()

def construct_df_reg(df, df_freqs, list_of_words):
    '''
    Objectifs:
    Construire le df qui va nous aider à faire nos régressions 

    Arguments:
    df_freqs -> DataFrame : le df des freqs
    '''
    for word in list_of_words:
        df[f'{word}'] = df['text'].apply(count_liste, args=(word,))
    return df 

def normalize(df, list_of_words):
    '''
    Objectifs:
    Normaliser les coeffs du Df 

    Arguments:
    df -> DataFrame : le df 
    '''
    df['somme'] = df.sum(axis=1)
    df.loc[df['somme'] == 0, 'somme'] = 1
    for word in list_of_words:
        df[f'{word}'] = df[f'{word}'] / df['somme'] 
    return df

def party_str_to_dummy(df):
  df.loc[df['party'] == 'Con', 'party_bool'] = 1
  df.loc[df['party'] == 'Lab', 'party_bool'] = 0
  return df 