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