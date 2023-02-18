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

def read_HouseOfCommons(keep_date, rd_lines=False, n=1000):
    '''
    Objectif:
    Cette fonction permet de lire la base des parlementaires 
    elle renvoie le dataFrame preprocessé
    Elle peut ne renvoyer qu'uniquement n random lines du df  (1000 par défaut)

    Arguments:
    keep_date -> bool qui détermine si on supprime la colonne keep_date
    df -> DataFrame : le DataFrame
    n -> int : le nb de lignes qu'on souhaite garder
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

def keep_parties(df, list_of_parties):
    '''
    Objectif:
    Cette fonction le df en ne gardant que les partis politiques choisis  

    Arguments:
    df -> DataFrame : le DataFrame avec les speechs
    list_of_parties -> list : liste des partis politiques qu'on souhaite garder
    '''
    return df.loc[df['party'].isin(list_of_parties)]