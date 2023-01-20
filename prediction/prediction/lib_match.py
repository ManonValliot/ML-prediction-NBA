"""Description.

Librairie qui construit un dataframe avec les dernières statistiques moyennes et la dernière évaluation Élo des équipes que l'utilisateur a indiqué.
"""


import pandas as pd


def _reindex_colonnes(data: pd.DataFrame) -> pd.DataFrame:
    """Retourne un dataframe où les statistiques de l'équipe à domicile sont collées entre elles et celles de l'équipes à l'extérieur également."""
    temp_cols = data.columns.tolist()
    new_cols = temp_cols[37:38] + temp_cols[0:18] + temp_cols[36:37] + temp_cols[18:36]
    return data[new_cols]


def _dernier_match(data: pd.DataFrame, team: str) -> pd.DataFrame:
    """Retourne le dernier match joué par l'équipe.

    Exemple :
    >>> _dernier_match(pd.DataFrame({'Date': ['Oct 9, 2014', 'Oct 9, 2014', 'Oct 23, 2014', 'Jun 13, 2015'], 'Team_Home': ['Miami Heat', 'Los Angeles Lakers', 'Miami Heat', 'Indiana Pacers'],'Team_Visitor': ['Chicago Bulls', 'Miami Heat', 'Phoenix Suns', 'Phoenix Suns']}), 'Miami Heat')
               Date   Team_Home  Team_Visitor
    2  Oct 23, 2014  Miami Heat  Phoenix Suns
    """
    derniers_matchs = data.loc[
        (data["Team_Home"] == team) | (data["Team_Visitor"] == team)
    ].tail(1)
    return derniers_matchs


def _reindex_colonnes_elo(data: pd.DataFrame) -> pd.DataFrame:
    """Retourne un dataframe où les statistiques de l'équipe à domicile sont collées entre elles et celles de l'équipes à l'extérieur également."""
    temp_cols = data.columns.tolist()
    new_cols = (
        temp_cols[1:3]
        + temp_cols[43:44]
        + temp_cols[3:21]
        + temp_cols[42:43]
        + temp_cols[21:39]
    )
    return data[new_cols]


def _stats_team_prediction(data: pd.DataFrame, team: str) -> pd.DataFrame:
    """Retourne les dernières statistiques moyennes de l'équipe demandée."""
    data_new = pd.DataFrame(
        columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    )
    data_dernier_match = _reindex_colonnes_elo(_dernier_match(data, team)).reset_index(
        drop=True
    )
    if data_dernier_match["Team_Home"][0] == team:
        data_tempo = data_dernier_match.iloc[:, 21:40]
        data_tempo.columns = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
        ]
        data_new = data_new.append(data_tempo)
    else:
        data_tempo = data_dernier_match.iloc[:, 2:21]
        data_tempo.columns = [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
        ]
        data_new = data_new.append(data_tempo)
    return data_new


def _creation_dataframe_prediction(data_predict: pd.DataFrame) -> pd.DataFrame:
    """Retourne un dataframe des variables prédictives avec les statistiques de l'équipe à domicile collées
    entre elles et celles de l'équipes à l'extérieur également."""
    liste = list(range(0, 38))
    data_predict.loc[len(data_predict)] = liste
    data = _reindex_colonnes(data_predict)
    return data


class Match_Predict:
    """Création de l'objet dataframe match à prédire."""

    def __init__(
        self,
        features: pd.DataFrame,
        team_home: str,
        team_visitor: str,
        data: pd.DataFrame,
    ):
        self.features = features
        self.team_home = team_home
        self.team_visitor = team_visitor
        self.data = data
        self.data_predict = pd.DataFrame(columns=[self.features.columns.to_list()])

    def __repr__(self):
        return f"Match_Predict(data_predict={repr(self.data_predict)})"

    def creation_ligne_prediction(self) -> pd.DataFrame:
        """Remplie l'objet Match_Predict aves les dernières statistiques moyennes des équipes de demandées."""
        data_predict = _creation_dataframe_prediction(self.data_predict)
        stats_h = _stats_team_prediction(self.data, self.team_home)
        stats_v = _stats_team_prediction(self.data, self.team_visitor)
        for colonne, stat in zip(range(19, 39), stats_h):
            data_predict.iloc[0, colonne] = stats_h.iloc[:, stat - 1]
        for colonne, stat in zip(range(0, 19), stats_v):
            data_predict.iloc[0, colonne] = stats_v.iloc[:, stat - 1]
        return data_predict
