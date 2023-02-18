import pandas as pd 
import statsmodels.api as sm

def regress_df(df, list_of_words):
    dico={}
    dico['Speaker'] = ['intercept', 'slope_coefficient']

    for word in list_of_words:
        x = df['party_bool']
        y = df[f'{word}']

        # adding the constant term
        x = sm.add_constant(x)

        result = sm.OLS(y, x).fit()

        dico[f'{word}'] = [result.params[0], result.params[1]]
    aux = pd.DataFrame(dico)
    df = pd.concat([df, aux]).reset_index(drop=True)
    df.drop(columns=['somme'], inplace=True)
    df = df[['Speaker', 'party', 'text']+['party_bool'] + list(df.columns)[3:-1]]
    return df 