import pandas as pd 
from src.utils import read_input

dtypes = {
    'party.facts.id' : str,
    'date': object,
    'agenda': object,
    'speechnumber': int,
    'speaker': object,
    'party': object,
    'party.facts.id': object,
    'chair': bool,
    'terms': int,
    'text': object,
}

def read_HouseOfCommons(keep_date: bool, rd_lines=False, n=1000):
    '''
    Cette fonction permet de lire la base des parlementaires 
    elle renvoie le dataFrame preprocessé
    Elle peut ne renvoyer qu'uniquement n random lines du df  (1000 par défaut)

    Parameters:
    -----------
    keep_date: détermine si on supprime la colonne keep_date
    n: le nb de lignes qu'on souhaite garder
    '''
    df = read_input('00. input/Corp_HouseOfCommons_V2_2010-2.csv', encod='ISO-8859-1', dtype_values=dtypes)
    if keep_date:
        df.drop(columns=['Unnamed: 0', 'iso3country', 'parliament', 'party.facts.id', 'speechnumber', 'chair', 'terms'], inplace=True)
    else:
        df.drop(columns=['Unnamed: 0', 'iso3country', 'parliament', 'party.facts.id', 'speechnumber', 'chair', 'terms', 'date'], inplace=True)
    df.rename(columns=
        {'speaker': 'Speaker'},
        inplace=True
    )
    if rd_lines:
        df = df.sample(frac=1).reset_index(drop=True)
        df = df.head(n)
        return df
    return df 

def keep_parties(df: pd.DataFrame, list_of_parties: list):
    '''
    Cette fonction le df en ne gardant que les partis politiques choisis  

    Parameters:
    -----------
    df : le DataFrame avec les speechs
    list_of_parties : liste des partis politiques qu'on souhaite garder
    '''
    return df.loc[df['party'].isin(list_of_parties)]

def read_and_prepare_df_of_the_model(path: str):
    '''
    this function reads the dataframe with the 500 significant words and their frequencies found 
    during the treatement of article 1. It prepares it and put it in shape to prepare the new model. 

    Parameters:
    -----------
    path: the path of the df_freqs obtained in the first model
    '''
    df = pd.read_csv(path)
    df.drop(columns=['Unnamed: 0', 'text'], inplace=True)
    new_df = pd.melt(df, id_vars=['Speaker', 'party'])
    new_df.sort_values(by=['variable'], inplace=True)
    new_df = new_df.reset_index(drop=True)
    return new_df