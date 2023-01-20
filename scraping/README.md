# Énoncé du dossier
Ces librairies permettent la phase de scraping du site `basketball-referance.com` et de récupérer les données sous forme csv. Les données récoltées concernent les matchs de saisons régulières de NBA, de 2006 à 2023. L'outil utiliser pour cette étape est `selenium`. Nous avons décider d'utiliser ce package puisque la récupération des données sur ce site nécessite énormément de naviguations et de changements de page.


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
