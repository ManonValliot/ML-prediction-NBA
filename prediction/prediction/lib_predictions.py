"""Description.

Librairie qui prédit l'issue d'un match de NBA.
"""


from .lib_match import Match_Predict
import pandas as pd
import numpy as np
import pickle
import warnings

warnings.simplefilter("ignore")


def creation_data(path: str) -> pd.DataFrame:
    """Retourne notre base de données."""
    data = pd.read_csv(path, sep=";")
    return data.reset_index(drop=True)


def creation_features(path: str) -> pd.DataFrame:
    """Retourne le dataframe avec les variables explicatives."""
    data = creation_data(path)
    features = data.drop(
        columns=[
            "Date",
            "Team_Home",
            "Team_Visitor",
            "Season",
            "Home_win",
            "Visitor_win",
            "Team_Home_Elo_After",
            "Team_Visitor_Elo_After",
        ]
    )
    return features


def prediction(path: str, team_home: str, team_visitor: str) -> np.array:
    """Retourne la prédiction d'un match, c'est-à-dire renvoie 1 si l'équipe à domicile gagne, sinon 0.

    Exemple :
    >>> prediction("data.csv", "Phoenix Suns", "Indiana Pacers")
    array([0])
    """
    features = creation_features(path)
    data = creation_data(path)
    prediction = Match_Predict(
        features, team_home, team_visitor, data
    ).creation_ligne_prediction()
    model_knn = pickle.load(open("knn_model.sav", "rb"))
    return model_knn.predict(prediction)


def proba(path: str, team_home: str, team_visitor: str) -> np.array:
    """Retourne les probabilités estimées par le modèle des classes.

    Exemple :
    >>> proba("data.csv", "Phoenix Suns", "Indiana Pacers")
    array([0.69230769, 0.30769231])
    """
    features = creation_features(path)
    data = creation_data(path)
    prediction = Match_Predict(
        features, team_home, team_visitor, data
    ).creation_ligne_prediction()
    model_knn = pickle.load(open("knn_model.sav", "rb"))
    proba = model_knn.predict_proba(prediction)[0]
    return proba
