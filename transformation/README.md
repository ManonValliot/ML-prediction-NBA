# Énoncé du dossier 
Cette librairie permet la phase de transformation de la base de données, récupérée sous forme de csv dans la partie scraping. Ces transfomations vont nous permettent de réaliser des prédictions sur l'issue des matchs. Plusieurs modifications ont alors été nécessaires. 

## Statistiques moyennes

Notre but étant de prédire l'issue d'un match, les modèles de prédiction ont été entrainés sur les statistiques moyennes des derniers matchs joués par chaque équipe. Les statistiques actuelles de chaque matchs ont donc été remplacées par les statistiques moyennes des 5 derniers matchs. Les matchs ne possédant pas assez de données antérieurs pour effectuer ces moyennes ont donc été supprimés. On observe alors une certaine perte d'informations.


## Évaluation Élo

Afin de perfectionner les prédictions, la méthode d'évaluation Élo des équipes a été ajoutée. Cette méthode permet d'évaluer les performances des équipes sur plusieurs saisons. Elo a été utiliser afin de pondérer, de manière appropriée, les victoires (et les défaites) de qualité, tout en reconnaissant que toutes les équipes ne sont pas créées égales. Cette évaluation prend en compte :  le score final de chaque match, l'endroit où il a été joué et la performance des équipes avant le match.



# Utilisation

Veuillez importer les éléments ci-dessous.
```bash
import pandas as pd
from lib_transformation import transformation_dataframe
```

Pour lancer les transformations et récupérer la nouvelle base de données sous forme csv , veuillez lancer la fonction ci-dessous en indiquant le path de destination et le nombre de matchs sur lequel vous voulez appliquer les statistiques moyennes.
```bash
data = pd.read_csv('scraping.csv', sep = ';')
transformation_dataframe(data, 5).to_csv('data.csv', index=False, header=True,sep=';',encoding='utf-8-sig')
```
