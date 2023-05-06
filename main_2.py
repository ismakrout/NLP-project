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
from src.modelisation_arcticle_2 import *

os.chdir('../')

# pour ne pas charger le NB avec des warnings 
import warnings 
warnings.filterwarnings('ignore')

def main_calcul_pi(df: pd.DataFrame):
    df_modelisation = read_and_prepare_df_of_the_model('01. output/df_freqs_speaker_word.csv')
    df_modelisation['m_it'] = df_modelisation.groupby(by=['Speaker', 'party'])['c_ijt'].transform('sum')
    # On Calcule les termes ds le sigma 
    df_modelisation['q_hat_it'] = df_modelisation['c_ijt']/df_modelisation['m_it']
    df_modelisation_Lab = df_modelisation.loc[df_modelisation['party'] == 'Lab']
    df_modelisation_Con = df_modelisation.loc[df_modelisation['party'] == 'Con']
    # ## plug-in estimator (biased)
    df_modelisation_Lab_plugin = plugin_estimator_by_party(df_modelisation_Lab, 'Lab')
    df_modelisation_Con_plugin = plugin_estimator_by_party(df_modelisation_Con, 'Con')
    df_modelisation_plugin = plugin_estimator(
        df_modelisation_Lab_plugin,
        df_modelisation_Con_plugin
    )
    # we compute pi
    pi_plugin = compute_pi_plugin(df_modelisation_plugin)
    # ## leave-out estimator (not biased)
    # We compute the q_ijt_column which serves to compute rho_hat_-ijt
    df_modelisation_Con_leave_out = compute_q_ijt_column(df_modelisation_Con, 'Con')
    df_modelisation_Lab_leave_out  = compute_q_ijt_column(df_modelisation_Lab, 'Lab')
    # we compute the rho_hat_-ijt column
    df_modelisation_Con_leave_out = compute_rho_hat_ijt_column(df_modelisation_Con_leave_out, df_modelisation_Lab_plugin, 'Con')
    df_modelisation_Lab_leave_out = compute_rho_hat_ijt_column(df_modelisation_Lab_leave_out, df_modelisation_Con_plugin, 'Lab')
    df_pi_word_Con_leave_out = create_df_pi_word_party(df_modelisation_Con_leave_out, "Con")
    df_pi_word_Lab_leave_out = create_df_pi_word_party(df_modelisation_Lab_leave_out, "Lab")
    df_modelisation_leave_out = pd.merge(
        df_pi_word_Con_leave_out,
        df_pi_word_Lab_leave_out,
        how='left',
        on=['variable'],
    )
    df_modelisation_leave_out['pi'] = df_modelisation_leave_out['moitie_Con_pi'] + df_modelisation_leave_out['moitie_Lab_pi']
    pi_leave_out = df_modelisation_leave_out['pi'].sum()
    return pi_leave_out

