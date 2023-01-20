# Énoncé du dossier

Ces librairies permettent la phase de prédiction. L'agorithme sélectionné pour cette étape est le K-Nearest Neighbors Classifier, car il a le meilleur
score de cross validation sans pour autant être en sur-apprentissage. Si vous souhaitez voir tous les modèles testés, veuillez consulter le fichier `selection_modele.ipynb`.


# Méthodologie des librairies

Pour résoudre ce problème de prédiction, nous avons créer plusieurs librairies avec leurs tests correspondants.

Librairie **lib_levenshtein.py**
> Permet de trouver le nom d'équipe le plus semblable à travers l'agorithme de Levenshtein. L'utilisateur peut écrire en majuscule, remplire trop d'espaces, 
des tirets, des accents ou des caractères spéciaux, cela ne sera pas pris en compte dans le calcul du ratio de similitude.

Librairie **lib_match.py**
> Permet de construire un dataframe avec les dernières statistiques moyennes et la dernière évaluation Élo des équipes que l'utilisateur a indiquées.

Librairie **lib_predictions.py**
> Permet de prédire l'issue d'un match de saison régulière de NBA.


# Utilsation de l'application

1. Télecharcher ce dossier pour l'importer dans votre ordinateur.
2. Depuis votre terminal, placez-vous dans le dossier importé.
3. Lancer l'application avec la commande ci-dessous.
```bash
python app.py
```
