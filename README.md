# NLP-project
During my masters, I've worked in a NLP research project with an Oxford doctor Christopher LeGaillac

In the first part of the project we've studied two econometric articles. The first one is quite basic. The second one introduces us to the logistic regression,
a classical technique in NLP.

Dans le package data_processing:
On va tout d'abord créer une fonction qui va appliquer le même traitement aux speeches qui a été appliqué aux textes des journaux : 
- tokenization 
- nettoyage de la ponctuation et des nombres 
- stemming des mots 
- nettoyage des stopwords à l'aide de la même liste que pour les journaux
- remise des mêmes stopwords significatifs que pour les journaux 

## Organisation des NB 
* Les NB_1 et NB_2 portent sur le premier article. 
    + Le NB_1 avec les speachs du parlement 
    + Le NB_2 sur les articles du daily news et de the guardian
* Les NB_3 et NB_4 portent sur le second article. 
    - Le NB_3 avec les speachs du parlement 
    - Le NB_4 sur les articles du daily news et de the guardian 
* Le NB_5 est la partie qui porte sur le ML
    - je vais entrainer sur toute la base et obtenir les 5000 mots les plus dits (mes futurs features)
    - je fais une réduction de dimension avec une ACP 
    - j'utiliserai peut être une pénalisation du type Lasso pour réduire le nombre de features 
    - puis j'applique un SVM et du decision tree avec du XGboost 

