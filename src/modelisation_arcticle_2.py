import pandas as pd 
import statsmodels.api as sm

#  ## functions linked to the plug-in estimator
def plugin_estimator_by_party(df: pd.DataFrame, party: str):
    '''
    allows to prepare one dataframe for each party in order to compute the plug-in estimator 
    (which is biased) of pi for every speaker 

    Parameters
    ----------
    df_plugin: the dataframe with the different frequencies of words of the speakers
    '''
    df_plugin = df.copy()
    df_plugin['Somme_m_it'] = df_plugin.groupby(by=['variable', 'party'])['m_it'].transform('sum')
    df_plugin['Somme_c_it'] = df_plugin.groupby(by=['variable', 'party'])['c_ijt'].transform('sum')
    df_plugin.drop_duplicates(subset=['variable'], inplace=True)
    df_plugin[f'q_hat_{party}_jt'] = df_plugin['Somme_c_it'] / df_plugin['Somme_m_it']
    df_plugin = df_plugin[['variable', f'q_hat_{party}_jt']].reset_index(drop=True)
    return df_plugin

def plugin_estimator(df_party_1: pd.DataFrame, df_party_2: pd.DataFrame):
    '''
    merge the df_modelisation_Con_plugin and the df_modelisation_Lab_plugin
    
    Parameters
    ----------
    df_party_1: df_modelisation_Lab_plugin
    df_party_2: df_modelisation_Con_plugin    
    '''
    df = pd.merge(
        df_party_1,
        df_party_2,
        how='left',
        on=['variable']
    )
    df['rho_hat_jt'] = df[f'q_hat_Con_jt'] / (df[f'q_hat_Con_jt'] + df[f'q_hat_Lab_jt'])
    return df

def compute_pi_plugin(df: pd.DataFrame):
    '''
    We apply the formula of the article 

    Parameters
    ----------
    df: df_modelisation_plugin
    '''
    pi = (1/2)*(df[f'q_hat_Con_jt']*df['rho_hat_jt']).sum() + (1/2)*(df[f'q_hat_Lab_jt']*(1-df['rho_hat_jt'])).sum()
    return pi

#  ## functions linked to the leave-out estimator
def compute_q_ijt_column(df: pd.DataFrame, party: str):
    '''
    compute the f'q_hat_{party}_-ijt' column
    
    Parameters
    ----------
    df: the Con or Lab dataframe
    party: Con if conservatif party and Lab if labor party
    '''
    df_modelisation = df.copy()
    df_modelisation['Somme_c_it'] = df_modelisation.groupby(by=['variable'])['c_ijt'].transform('sum')
    df_modelisation['Somme_c_it'] = df_modelisation['Somme_c_it'] - df_modelisation['c_ijt']

    df_modelisation['Somme_m_it'] = df_modelisation.drop_duplicates(subset=['Speaker'])['m_it'].sum()
    df_modelisation['Somme_m_it'] = df_modelisation['Somme_m_it'] - df_modelisation['m_it']
    df_modelisation[f'q_hat_{party}_-ijt'] = df_modelisation['Somme_c_it'] / df_modelisation['Somme_m_it']
    
    return df_modelisation