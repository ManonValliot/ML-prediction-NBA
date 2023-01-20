"""Description.

Librairie qui transforme une base de données.
Les transformations effectuées sont : 
- l'ajout de colonnes winner
- l'ajout d'une colonne saison
- l'ajout de colonnes évaluation Elo
- remplacement des statistiques d'un match par les statistiques moyennes des n derniers matchs.
"""

import pandas as pd
import math
import datetime as dt


def get_winner(points_home: int, points_visitor: int) -> tuple[list]:
    """Fonction qui ajoute des colonnes winner pour l'équipe à domicile et l'équipe extérieur.

    Exemple :
    >>> get_winner(115, 188)
    (0, 1)
    """
    if (points_home - points_visitor) > 0:
        home_win = 1
        visitor_win = 0
    else:
        home_win = 0
        visitor_win = 1
    return home_win, visitor_win


def get_season(Date: dt) -> str:
    """Fonction qui détermine la saison associée à la date.

    Exemple :
    >>> get_season(dt.date(2014, 10, 9))
    '2014-2015'
    """
    if Date.month in [9, 10, 11, 12]:
        return str(Date.year) + "-" + str(Date.year + 1)
    else:
        return str(Date.year - 1) + "-" + str(Date.year)


def uniformisation_nom_team(nom_team_home: str, nom_team_visitor: str) -> tuple[list]:
    """Fonction qui uniformise le nom des équipes selon les saisons."""
    if nom_team_home == "New Orleans/Oklahoma City Hornets":
        nom_team_home = "New Orleans Hornets"
    elif nom_team_visitor == "New Orleans/Oklahoma City Hornets":
        nom_team_visitor = "New Orleans Hornets"
    else:
        pass


def e_team(home_elo: float, visitor_elo: float, avantage_terrain: int) -> tuple[float]:
    """Retourne la probabilté de victoire des équipes.

    Exemple :
    >>> e_team(1500, 1567.45, 75)
    (0.5108636134525542, 0.4891363865474459)
    """
    home_rating = math.pow(10, (home_elo + avantage_terrain) / 400)
    visitor_rating = math.pow(10, (visitor_elo) / 400)
    e_home = home_rating / (home_rating + visitor_rating)
    e_visitor = visitor_rating / (home_rating + visitor_rating)
    return e_home, e_visitor


def k_elo(marge_points: int, elo_difference: float) -> float:
    """Calcul la constante mobile qui dépend de la marge de victoire et de la différence de classement Elo.

    Exemple :
    >>> k_elo(15, 67.78)
    25.54193747316395
    """
    if marge_points > 0:
        k = 20 * ((marge_points + 3) ** (0.8) / (7.5 + 0.006 * (elo_difference)))
    else:
        k = 20 * ((-marge_points + 3) ** (0.8) / (7.5 + 0.006 * (-elo_difference)))
    return k


def elo_after(
    points_home: int,
    points_visitor: int,
    home_win: int,
    visitor_win: int,
    home_elo: float,
    visitor_elo: float,
    avantage_terrain: int,
) -> tuple[float]:
    """Calcul l'évaluation Elo après un match.

    Exemple :
    >>> elo_after(78, 112, 0, 1, 1512.3, 1597.89, 75)
    (1490.5580867390158, 1619.6319132609842)
    """
    k = k_elo((points_home - points_visitor), (home_elo - visitor_elo))
    e_home = e_team(home_elo, visitor_elo, avantage_terrain)[0]
    e_visitor = e_team(home_elo, visitor_elo, avantage_terrain)[1]
    elo_after_home = home_elo + k * (home_win - e_home)
    elo_after_visitor = visitor_elo + k * (visitor_win - e_visitor)
    return elo_after_home, elo_after_visitor


def premier_elo(
    liste_teams: list[str], team_home: str, team_visitor: str
) -> tuple[list]:
    """Applique une évaluation Elo de 1500 pour le premier match de chaque équipe.

    Exemple :
    >>> premier_elo(['Phoenix Suns', 'Indiana Pacers'], 'Phoenix Suns', 'New York Knicks')
    (False, 1500)
    """
    if liste_teams.count(team_home) == 0:
        Home_Elo_Before = 1500
    else:
        Home_Elo_Before = False
    if liste_teams.count(team_visitor) == 0:
        Visitor_Elo_Before = 1500
    else:
        Visitor_Elo_Before = False
    return Home_Elo_Before, Visitor_Elo_Before


def dernier_index(liste: list[str], element: str) -> int:
    """Retourne le dernier élément choisi d'une liste avec des doublons.

    Exemple :
    >>> dernier_index(['Phoenix Suns', 'Indiana Pacers', 'New York Knicks', 'New York Knicks', 'Phoenix Suns'], 'Phoenix Suns')
    4
    """
    indices = [index for index, item in enumerate(liste) if item == element]
    if len(indices) == 0:
        max_indice = -1
    else:
        max_indice = max(indices)
    return max_indice


def elo_saison_suivante(elo_after: float) -> float:
    """Retourne l'évaluation Elo de la saison suivante.

    Exemple :
    >>> elo_saison_suivante(1567.95)
    1552.2125
    """
    elo = (0.75 * elo_after) + (0.25 * 1505)
    return elo


def reindex_colonnes(data: pd.DataFrame) -> pd.DataFrame:
    """Retourne un dataframe où les statistiques de l'équipe à domicile sont collées entre elles et celles de l'équipes à l'extérieur également."""
    temp_cols = data.columns.tolist()
    new_cols = temp_cols[:4] + temp_cols[5:22] + temp_cols[4:5] + temp_cols[22:]
    return data[new_cols]


def derniers_matchs(data: pd.DataFrame, team: str, index: int, n: int) -> pd.DataFrame:
    """Retourne les derniers matchs joués par l'équipe.

    Exemple :
    >>> derniers_matchs(pd.DataFrame({'Date': [dt.date(2014, 10, 9), dt.date(2014, 10, 9), dt.date(2015, 8, 12), dt.date(2015, 4, 2)], 'Team_Home': ['Miami Heat', 'Los Angeles Lakers', 'Miami Heat', 'Indiana Pacers'],'Team_Visitor': ['Chicago Bulls', 'Miami Heat', 'Phoenix Suns', 'Phoenix Suns']}), 'Miami Heat', 2, 2)
    /Users/manonvalliot/Documents/M2/Projet_ML/Transformation/lib_transformation.py:145: UserWarning: Boolean Series key will be reindexed to match DataFrame index.
             Date           Team_Home   Team_Visitor
    0  2014-10-09          Miami Heat  Chicago Bulls
    1  2014-10-09  Los Angeles Lakers     Miami Heat
    """
    derniers_matchs = data.loc[data["Date"] < data["Date"][index]][
        (data["Team_Home"] == team) | (data["Team_Visitor"] == team)
    ].tail(n)
    return derniers_matchs


def stats_moyennes(data: pd.DataFrame, team: str, index: int, n: int) -> pd.Series:
    """Retourne les statistiques moyennes des derniers matchs de l'équipe.

    Exemple :
    >>> stats_moyennes(data, 'Chicago Bulls', 291, 5)
    1     107.4000
    2      40.4000
    3      79.6000
    4       0.5078
    5       7.2000
    6      18.6000
    7       0.3848
    8      19.4000
    9      28.6000
    10      0.6792
    11     10.4000
    12     34.4000
    13     44.8000
    14     25.4000
    15      8.2000
    16      6.6000
    17     13.8000
    18     25.6000
    dtype: float64
    """
    data_reindex = reindex_colonnes(data)
    data_derniers_matchs = derniers_matchs(data_reindex, team, index, n)
    data_new = pd.DataFrame(
        columns=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    )
    data_h = data_derniers_matchs.iloc[:, 21:39]
    data_v = data_derniers_matchs.iloc[:, 3:21]
    data_v.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    data_h.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    data = data_derniers_matchs.reset_index(drop=True)
    for ligne in range(len(data_derniers_matchs)):
        if data["Team_Home"][ligne] == team:
            data_new = data_new.append(data_h.iloc[ligne, :])
        else:
            data_new = data_new.append(data_v.iloc[ligne, :])
    return data_new.mean()


def applique_stats_moyennes(data: pd.DataFrame, n: int) -> pd.DataFrame:
    """Remplaces les statistiques des équipes pour un match par les statistiques moyennes à l'ensemble d'un dataframe."""
    new_data = reindex_colonnes(data.copy()).reset_index(drop=True)
    data = data.reset_index(drop=True)
    for ligne in data.index:
        team_h = data["Team_Home"][ligne]
        stat_h = stats_moyennes(data, team_h, ligne, n)
        for colonne, stat in zip(range(21, 39), stat_h):
            new_data.iloc[ligne, colonne] = stat
        team_v = data["Team_Visitor"][ligne]
        stat_v = stats_moyennes(data, team_v, ligne, n)
        for colonne, stat in zip(range(3, 21), stat_v):
            new_data.iloc[ligne, colonne] = stat
    return new_data.dropna().reset_index(drop=True)


def applique_stats_moyennes_par_saison(data: pd.DataFrame, n: int) -> pd.DataFrame:
    """Applique les statistiques moyennes pour chaque match en distinguant les saisons."""
    saison_data = pd.DataFrame()
    for saison in data["Season"].unique():
        saison_stats = applique_stats_moyennes(data[data["Season"] == saison], n)
        saison_data = saison_data.append(saison_stats)
    return saison_data.reset_index(drop=True)


def initialisation_colonnes(data: pd.DataFrame) -> pd.DataFrame:
    """Transforme le type de la colonne 'date' en date et ajoute des nouvelles colonnes.

    Exemple :
    >>> initialisation_colonnes(pd.DataFrame({'Date': ['Oct 31, 2006', 'Oct 31, 2006', 'Oct 31, 2006', 'Oct 31, 2006']}))
            Date     Season Home_win Visitor_win Team_Home_Elo_Before Team_Visitor_Elo_Before Team_Home_Elo_After Team_Visitor_Elo_After
    0 2006-10-31  2006-2007
    1 2006-10-31  2006-2007
    2 2006-10-31  2006-2007
    3 2006-10-31  2006-2007
    """
    data["Date"] = pd.to_datetime(data["Date"])
    data["Season"] = data["Date"].apply(get_season)
    data["Home_win"] = ""
    data["Visitor_win"] = ""
    data["Team_Home_Elo_Before"] = ""
    data["Team_Visitor_Elo_Before"] = ""
    data["Team_Home_Elo_After"] = ""
    data["Team_Visitor_Elo_After"] = ""
    return data


def elo_before(data: pd.DataFrame, ligne: int, index1: int, index2: int) -> tuple[list]:
    """Affecte l'ancien elo des équipes si ce n'est pas leur premier match.

    Exemple :
    >>> elo_before(pd.DataFrame({'Date': [dt.date(2014, 10, 9), dt.date(2014, 10, 9), dt.date(2015, 8, 12), dt.date(2015, 4, 2)], 'Season': ['2014-2015', '2014-2015', '2014-2015', '2014-2015'], 'Team_Home': ['Miami Heat', 'Los Angeles Lakers', 'Miami Heat', 'Indiana Pacers'],'Team_Visitor': ['Chicago Bulls', 'Miami Heat', 'Phoenix Suns', 'Phoenix Suns'], 'Team_Home_Elo_Before': [1500, 1500, False, 1500], 'Team_Visitor_Elo_Before': [1500, 1604.345, 1500, False], 'Team_Visitor_Elo_After': [1527, 1508.76, "", ""], 'Team_Home_Elo_After': [1604.345, 1598.76, "", ""]}), 2, pd.DataFrame({'Date': [dt.date(2014, 10, 9), dt.date(2014, 10, 9), dt.date(2015, 8, 12), dt.date(2015, 4, 2)], 'Season': ['2014-2015', '2014-2015', '2014-2015', '2014-2015'], 'Team_Home': ['Miami Heat', 'Los Angeles Lakers', 'Miami Heat', 'Indiana Pacers'],'Team_Visitor': ['Chicago Bulls', 'Miami Heat', 'Phoenix Suns', 'Phoenix Suns'], 'Team_Home_Elo_Before': [1500, 1500, False, 1500], 'Team_Visitor_Elo_Before': [1500, 1604.345, 1500, False], 'Team_Visitor_Elo_After': [1527, 1508.76, "", ""], 'Team_Home_Elo_After': [1604.345, 1598.76, "", ""]})['Team_Home_Elo_Before'][2], 1, 0)
    1508.76
    """
    if index1 >= index2 and data["Season"][index1] != data["Season"][ligne]:
        return elo_saison_suivante(data["Team_Visitor_Elo_After"][index1])
    elif index1 >= index2:
        return data["Team_Visitor_Elo_After"][index1]
    elif index2 > index1 and data["Season"][index2] != data["Season"][ligne]:
        return elo_saison_suivante(data["Team_Home_Elo_After"][index2])
    else:
        return data["Team_Home_Elo_After"][index2]


def transformation_dataframe(data: pd.DataFrame, n: int) -> pd.DataFrame:
    """Applique des transformations sur un dataframe.

    Explication :
    La boucle explicite de cette fonction est nécessaire car il faut appliquer les étapes suivantes dans l'ordre
    et dans l'ordre des lignes, car la fonction regarde des observations passés à des index différents.
    """
    data = initialisation_colonnes(data)
    liste_teams = []
    liste_teams_home = []
    liste_teams_visitor = []
    for ligne in data.index:
        winner = get_winner(data["Points_Home"][ligne], data["Points_Visitor"][ligne])
        data["Home_win"][ligne] = winner[0]
        data["Visitor_win"][ligne] = winner[1]
        elo = premier_elo(
            liste_teams, data["Team_Home"][ligne], data["Team_Visitor"][ligne]
        )
        data["Team_Home_Elo_Before"][ligne] = elo[0]
        data["Team_Visitor_Elo_Before"][ligne] = elo[1]
        liste_teams.append(data["Team_Home"][ligne])
        liste_teams.append(data["Team_Visitor"][ligne])
        index1_home = dernier_index(liste_teams_visitor, data["Team_Home"][ligne])
        index2_home = dernier_index(liste_teams_home, data["Team_Home"][ligne])
        index1_visitor = dernier_index(liste_teams_visitor, data["Team_Visitor"][ligne])
        index2_visitor = dernier_index(liste_teams_home, data["Team_Visitor"][ligne])
        if data["Team_Home_Elo_Before"][ligne] == False:
            data["Team_Home_Elo_Before"][ligne] = elo_before(
                data, ligne, index1_home, index2_home
            )
        else:
            pass
        if data["Team_Visitor_Elo_Before"][ligne] == False:
            data["Team_Visitor_Elo_Before"][ligne] = elo_before(
                data, ligne, index1_visitor, index2_visitor
            )
        else:
            pass
        data["Team_Home_Elo_After"][ligne] = elo_after(
            data["Points_Home"][ligne],
            data["Points_Visitor"][ligne],
            data["Home_win"][ligne],
            data["Visitor_win"][ligne],
            data["Team_Home_Elo_Before"][ligne],
            data["Team_Visitor_Elo_Before"][ligne],
            75,
        )[0]
        data["Team_Visitor_Elo_After"][ligne] = elo_after(
            data["Points_Home"][ligne],
            data["Points_Visitor"][ligne],
            data["Home_win"][ligne],
            data["Visitor_win"][ligne],
            data["Team_Home_Elo_Before"][ligne],
            data["Team_Visitor_Elo_Before"][ligne],
            75,
        )[1]
        liste_teams_home.append(data["Team_Home"][ligne])
        liste_teams_visitor.append(data["Team_Visitor"][ligne])
    new_data = applique_stats_moyennes_par_saison(data)
    return new_data
