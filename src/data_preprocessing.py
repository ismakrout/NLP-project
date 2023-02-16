import pandas as pd 
from utils import read_input

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

def read_HouseOfCommons(path):
    df = read_input('00. input/Corp_HouseOfCommons_V2_2010-2.csv', encod='ISO-8859-1', dtype_values=dtypes)
    df.drop(columns=['Unnamed: 0', 'iso3country', 'parliament', 'party.facts.id', 'speechnumber', 'chair', 'terms', 'date'], inplace=True)
    df.rename(columns=
        {'speaker': 'Speaker'},
        inplace=True
    )
    return df 

