# Utilisation

Dans cette partie on transforme le dataframe, récupérer sous forme de csv dans la partie scraping, pour inclure les évaluations Elo des équipes de chaque match et pour remplacer les statistiques de chaque match par les statistiques moyennes des derniers matchs effectués par les équipes. Pour se faire, veuillez importer les éléments ci-dessous.
```bash
import pandas as pd
from lib_transformation import transformation_dataframe
```

Pour lancer les transformations et récupérer la nouvelle base de données sous forme csv , veuillez lancer la fonction ci-dessous en indiquant le path de destination et le nombre de match sur lequel vous voulez appliquer les statistiques moyennes.
```bash
data = pd.read_csv('test.csv', sep = ';')
transformation_dataframe(data, 5).to_csv('data.csv', index=False, header=True,sep=';',encoding='utf-8-sig')
```
