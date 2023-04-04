import pandas as pd
import numpy as np
import csv 
import matplotlib.pyplot as plt
import spacy
import math
import os
import statsmodels.api as sm

from src.utils import *
from src.data_preprocessing import *
from src.data_processing import *
from src.feature_selection import *
from src.modelisation_arcticle_1 import *

os.chdir('/Users/ismailakrout/Desktop/python/NLP_statapp')

# ## Data pre-processing 

# On lit la base des speechs
# on peut la rendre plus petite pour faire des tests 
df = read_HouseOfCommons(keep_date=False, rd_lines=True, n=1000)

# on ne garde que Labor et Conservative
df = keep_parties(df, ['Lab', 'Con'])

# ## Data processing

# On construit la liste des mots jugés non significatifs
stop_words = construct_list_stopwords()

# On cleen les titres des speechs
df['agenda'] = df['agenda'].apply(clean, args=(stop_words,))

# On construit las liste cleen des topics
list_stem_topics = process_list_BigTech_words(topics)

# On filtre le df et on garde uniquement les speechs sur les BigTech
df = keep_Bigtech_speeches(df, list_stem_topics)

df['text'] = df['text'].apply(clean, args=(stop_words,))

# On fait le groupby() par speaker et party par la suite pour ne pas dépasser les 1 000 000 carc 
df = df.groupby(by=['Speaker', 'party']).sum().reset_index()

# On va repérer les 100 mots (puis 500 quand on aura les speeches en entier) qui sont le plus 
# utilisés par chaque parti, et noter leur fréquence d'apparition. 

df_freqs_Con = count_freqs(df, 'Con')
df_freqs_Lab = count_freqs(df, 'Lab')

# On a tous les mots utilisés par le parti Conservateur sur les sujets définis, ainsi que leurs
#  fréquences d'apparition. On va retenir les fréquences avec lesquelles chaques mots sont utilisés,
#  par chaque parti, afin de déterminer le chi2 de chaque mot. On se restreint pour l'instant aux 
# partis Con et Lab, fortement majoritaires. 

df_freqs = merge_freq(df_freqs_Con, df_freqs_Lab)

# ## feature selection 

# On effectue le etst du Qi 2 
df_freqs = test_qi_2(df_freqs)

# On a donc ici chaque mot utilisé par les parti sur le sujet délimité, avec le chi2 correspondant.
#  On va se limiter aux 500 premiers mots :

df_freqs = keep_significatif_word(df_freqs, n=500)

# ## data processing bis

list_of_words = selected_words(df_freqs)
df = construct_df_reg(df, df_freqs, list_of_words)
# df.to_csv('01. output/df_freqs_speaker_word.csv')

df = normalize(df, list_of_words)
df = party_str_to_dummy(df)

# ## Regressions linéaires (Modélisation)

# rajout des lignes slopes_coeff et intercept
df = regress_df(df, list_of_words)
# df.to_csv('01. output/df_500_with_slope_coef_bis.csv')
