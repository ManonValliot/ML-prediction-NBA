# Énoncé du dossier
Ces librairies permettent la phase de scraping du site `basketball-referance.com` et de récupérer les données sous forme csv. Les données récoltées concernent les matchs de saisons régulières de NBA, de 2006 à 2023. L'outil utiliser pour cette étape est `selenium`. Nous avons décider d'utiliser ce package puisque la récupération des données sur ce site nécessite énormément de naviguations et de changements de page.


# Méthodologie des librairies

Pour résoudre effectuer le scraping, plusieurs librairies ont été effectuées.

Librairie **lib_driver.py**
> Permet la construction d'un driver et son initialisation à partir d'un lien.

Librairie **lib_BDD_box_score.py**
> Permet de construire une base de données à partir des résultats des matchs de NBA sur le site `basketball-referance.com`. Ces données représentent des informations complémentaires sur les matchs, comme le nombre de rebonds, etc. Ces informations ont été récupérées dans un hyperlien, nommé "box score", présent pour chaque match du tableau initial.

Librairie **lib_BDD_principale.py**
> Permet de construire une base de données à partir des résultats des matchs de NBA sur le `basketball-referance.com`. Ces données représentent les informations principales : la date du match, les équipes en jeu et leur points associés.

Librairie **lib_creation_dataframe.py**
> Permet de construire un dataframe, sous forme csv, avec les informations, principales et secondaires,  des résultats des matchs de NBA sur le site `basketball-referance.com`.


# Utilisation

Pour récupérer un csv avec les données des matchs de saison régulière de NBA, veuillez importer ces éléments ci-dessous.
```bash
from lib_driver import Driver
from lib_creation_dataframe import conversion_csv
```


Pour lancer le scraping et récupérer les données, veuillez lancer la fonction ci-dessous en indiquant le path de destination et les années de scrape souhaitées.
```bash
conversion_csv(Driver, r'/Users/manonvalliot/Documents/M2/scraping.csv', 2006, 2023)
```
