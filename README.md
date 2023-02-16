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
