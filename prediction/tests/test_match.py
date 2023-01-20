"""
Description.

Tests automatiques de la librairie lib_match.py
"""

import pandas as pd
from prediction.lib_predictions import creation_data, creation_features
from prediction.lib_match import (
    Match_Predict,
    _reindex_colonnes,
    _dernier_match,
    _reindex_colonnes_elo,
    _stats_team_prediction,
    _creation_dataframe_prediction,
)


def test_reindex_colonnes():
    data = _reindex_colonnes(creation_data("data.csv"))
    assert all(data) == True


def test_reindex_colonnes_false():
    data = _reindex_colonnes(creation_data("data.csv"))
    assert all(data) != False


def test_reindex_colonnes_longueur():
    data = _reindex_colonnes(creation_data("data.csv"))
    assert len(data) == len(creation_data("data.csv"))


def test_reindex_colonnes_longueur_false():
    data = _reindex_colonnes(creation_data("data.csv"))
    assert len(data) != len(creation_data("data.csv")) + 1


def test_dernier_match():
    data = _dernier_match(creation_data("data.csv"), "Miami Heat")
    assert all(data) == True


def test_dernier_match_false():
    data = _dernier_match(creation_data("data.csv"), "Miami Heat")
    assert all(data) != False


def test_dernier_match_longueur():
    data = _dernier_match(creation_data("data.csv"), "Miami Heat")
    assert len(data) == 1


def test_dernier_match_longueur_flase():
    data = _dernier_match(creation_data("data.csv"), "Miami Heat")
    assert len(data) != 2


def test_reindex_colonnes_elo():
    data = _reindex_colonnes_elo(creation_data("data.csv"))
    assert all(data) == True


def test_reindex_colonnes_elo_false():
    data = _reindex_colonnes_elo(creation_data("data.csv"))
    assert all(data) != False


def test_reindex_colonnes_elo_longueur():
    data = _reindex_colonnes_elo(creation_data("data.csv"))
    assert len(data) == len(creation_data("data.csv"))


def test_reindex_colonnes_elo_longueur_false():
    data = _reindex_colonnes_elo(creation_data("data.csv"))
    assert len(data) != len(creation_data("data.csv")) + 1


def test_stats_team_prediction():
    stats = _stats_team_prediction(creation_data("data.csv"), "Miami Heat")
    assert all(stats) == True


def test_stats_team_prediction_false():
    stats = _stats_team_prediction(creation_data("data.csv"), "Miami Heat")
    assert all(stats) != False


def test_stats_team_prediction_longueur():
    stats = _stats_team_prediction(creation_data("data.csv"), "Miami Heat")
    assert len(stats) == 1


def test_rstats_team_prediction_longueur_false():
    stats = _stats_team_prediction(creation_data("data.csv"), "Miami Heat")
    assert len(stats) != 2


def test_creation_dataframe_prediction():
    data = _creation_dataframe_prediction(
        pd.DataFrame(columns=[creation_features("data.csv").columns.to_list()])
    )
    assert all(data) == True


def test_creation_dataframe_prediction():
    data = _creation_dataframe_prediction(
        pd.DataFrame(columns=[creation_features("data.csv").columns.to_list()])
    )
    assert all(data) != False


def test_repr():
    features = creation_features("data.csv")
    data = creation_data("data.csv")
    match = Match_Predict(features, "Miami Heat", "Phoenix Suns", data)
    assert all(repr(match)) == True


def test_creation_ligne_prediction():
    features = creation_features("data.csv")
    data = creation_data("data.csv")
    match = Match_Predict(
        features, "Miami Heat", "Phoenix Suns", data
    ).creation_ligne_prediction()
    assert all(match) == True


def test_creation_ligne_prediction_false():
    features = creation_features("data.csv")
    data = creation_data("data.csv")
    match = Match_Predict(
        features, "Miami Heat", "Phoenix Suns", data
    ).creation_ligne_prediction()
    assert all(match) != False
