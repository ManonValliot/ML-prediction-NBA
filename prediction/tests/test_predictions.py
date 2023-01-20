"""
Description.

Tests automatiques de la librairie lib_prediction.py
"""


from prediction.lib_predictions import (
    prediction,
    proba,
    creation_data,
    creation_features,
)


def test_prediction():
    pred = prediction("data.csv", "Phoenix Suns", "Indiana Pacers")
    assert pred == [0]


def test_prediction_false():
    pred = prediction("data.csv", "Phoenix Suns", "Indiana Pacers")
    assert pred != [1]


def test_proba():
    probas = proba("data.csv", "Phoenix Suns", "Indiana Pacers")
    assert all(probas) == True


def test_proba_false():
    probas = proba("data.csv", "Phoenix Suns", "Indiana Pacers")
    assert all(probas) != False


def test_creation_data():
    data = creation_data("data.csv")
    assert all(data) == True


def test_creation_data_false():
    data = creation_data("data.csv")
    assert all(data) != False


def test_creation_features():
    data = creation_features("data.csv")
    assert all(data) == True


def test_creation_data_false():
    data = creation_features("data.csv")
    assert all(data) != False
