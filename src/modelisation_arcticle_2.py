import pandas as pd 
import statsmodels.api as sm

def plugin_estimator(df: pd.DataFrame):
    '''
    allows to compute the plug-in estimator (which is biased) of pi for every speaker 

    Parameters
    ----------
    df_plugin: the dataframe with the different frequencies of words of the speakers
    '''
    df_plugin = df.copy()
    df_plugin['Somme_m_it'] = df_plugin.groupby(by=['Speaker', 'party'])['m_it'].transform('sum')
    df_plugin['Somme_c_it'] = df_plugin.groupby(by=['Speaker', 'party'])['value'].transform('sum')
    df_plugin['q_hat_Lab_jt'] = df_plugin['Somme_c_it'] / df_plugin['Somme_m_it']
    df_plugin = df_plugin[['variable', 'q_hat_Lab_jt']]
    df_plugin.drop_duplicates(subset=['variable'], inplace=True)
    return df_plugin