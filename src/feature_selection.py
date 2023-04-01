import pandas as pd

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