import pandas as pd

from src.utils import *
from src.data_preprocessing import *
from src.data_processing import *
from src.feature_selection import *
from src.modelisation_arcticle_1 import *
from src.modelisation_arcticle_2 import *


# Correction du test du Qi 2 
def test_qi_2(df_freqs: pd.DataFrame):
    '''
    rajoute la colonne qi_2 au DataFrame df_freqs

    Paraneters:
    -----------
    df_freqs : la df des freq
    '''
    df_freqs.loc[df_freqs['freq_Con'].notna(), 'fp_Con'] = df_freqs.loc[df_freqs['freq_Con'].notna(), 'freq_Con']
    df_freqs['fp_Con'] = df_freqs['fp_Con'].fillna(0)

    df_freqs.loc[df_freqs['freq_Lab'].notna(), 'fp_Lab'] = df_freqs.loc[df_freqs['freq_Lab'].notna(), 'freq_Lab']
    df_freqs['fp_Lab'] = df_freqs['fp_Lab'].fillna(0)

    s_con = df_freqs['fp_Con'].sum()
    df_freqs['not_fp_Con'] = s_con - df_freqs['fp_Con']

    s_lab = df_freqs['fp_Lab'].sum()
    df_freqs['not_fp_Lab'] = s_lab - df_freqs['fp_Lab']

    df_freqs['chi_2'] = ((df_freqs['fp_Con'] * df_freqs['not_fp_Con'] - df_freqs['fp_Lab'] * df_freqs['not_fp_Lab'])**2) / ((df_freqs['fp_Con']+df_freqs['fp_Lab']) * (df_freqs['not_fp_Lab']+df_freqs['fp_Lab']) * (df_freqs['not_fp_Con']+df_freqs['fp_Con']) * (df_freqs['not_fp_Con']+df_freqs['not_fp_Lab']))

    df_freqs.drop(columns=['fp_Con', 'fp_Lab', 'not_fp_Con', 'not_fp_Lab'], inplace=True)

    return df_freqs

def keep_significatif_word(df_freqs: pd.DataFrame, n=500):
    '''
    garde les mots significatifs

    Paraneters:
    -----------
    df_freqs : le df des freq
    n : le nombre de mots qu'on souhaite garder
    '''
    df_freqs = df_freqs.sort_values(by=['chi_2'], ascending=False)
    df_freqs = df_freqs.head(n)
    return df_freqs

#############################################
### feature selection for the ML approach ###
#############################################

def select_features_with_freqs(df, rd_lines=True, n=10000):
    '''
    allows to choose the features ie the words with the highest frequency 
    '''
    df['agenda'] = df['agenda'].apply(clean, args=('unigram',))
    list_stem_topics = process_list_BigTech_words(topics)
    df['text'] = df['text'].apply(clean, args=('bigram',))
    df = df.groupby(by=['Speaker', 'party']).sum().reset_index()
    df_freqs_Con = count_freqs(df, 'Con')
    df_freqs_Lab = count_freqs(df, 'Lab')
    df_freqs = merge_freq(df_freqs_Con, df_freqs_Lab)
    return df_freqs