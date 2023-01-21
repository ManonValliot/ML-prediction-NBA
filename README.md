# Démarrage

Ce projet porte sur la création d'une application permettant de trouver l'issue d'un match de saison régulière de NBA. Le modèle sélectionné pour effectuer ces prédictions est l'algorithme K-Nearest Neighbors Classifier. Ce projet est achevé, cependant une amélioration peut être faîte sur l'inclusion des étapes de scraping et de transformation de base de données dans l'application pour ajouter les dernier matchs joués non inclus dans la base de données existante. 

# Démonstration

Afin de visualiser l'application, voici une démonstration de son application :

[Démonstration](https://user-images.githubusercontent.com/94387843/213761418-7e2be5b3-d5cf-4316-bfd9-2c69b2c4c922.mov)



# Méthodologie des dossiers

Pour résoudre le problème de prédiction d'issue de match NBA, nous avons crées plusieurs dossiers.

Dossier **scraping**
> Permet la phase de scraping du site `basketball-referance.com` et de récupérer les données sous forme csv.

Dossier **transformation**
> Permet de transformer la base de données scraper. Les modifications effectuées sont : l'ajout de colonnes winner, l'ajout d'une colonne saison, l'ajout de colonnes évaluation Elo et le remplacement des statistiques d'un match par les statistiques moyennes des n derniers matchs.

Dossier **prediction**
> Dossier contenant la sélection du meilleur modèle de prédiction ainsi que l'utilisation de ce modèle à travers l'application.

# Utilisation de l'application

L'application et les fichiers nécessaires à son fonctionnement sont dans le dossier `prediction`. 

1. Télecharcher le dossier `prediction` pour l'importer dans votre ordinateur.
2. Depuis votre terminal, placez-vous dans le dossier `prediction`.
3. Lancer l'application avec la commande ci-dessous.
```bash
python app.py
```
