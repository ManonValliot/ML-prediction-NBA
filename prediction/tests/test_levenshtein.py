"""
Description.

Tests automatiques de la librairie lib_levenshtein.py
"""

from prediction.lib_levenshtein import (
    minuscule,
    supprime_caracteres,
    enleve_accents,
    remplace_tiret,
    supprime_espaces_excessifs,
    nouveau_mot,
    ratio_similarite,
    attribution_teams,
)


def test_minuscule():
    mot = minuscule("CHaPeau")
    assert mot == "chapeau"


def test_minuscule_false():
    mot = minuscule("CHaPeau")
    assert mot != "chapeAu"


def test_supprime_caracteres():
    mot = supprime_caracteres("informa&tique%")
    assert mot == "informatique"


def test_supprime_caracteres_false():
    mot = supprime_caracteres("informa&tique%")
    assert mot != "informatique%"


def test_enleve_accents():
    mot = enleve_accents("prédiction")
    assert mot == "prediction"


def test_enleve_accents_false():
    mot = enleve_accents("prédiction")
    assert mot != "prédiction"


def test_remplace_tiret():
    mot = remplace_tiret("New-Orleans")
    assert mot == "New Orleans"


def test_remplace_tiret_false():
    mot = remplace_tiret("New-Orleans")
    assert mot != "NewmOrleans"


def test_supprime_espaces_excessifs():
    mot = supprime_espaces_excessifs("Octobre   31,  2022  ")
    assert mot == "Octobre 31, 2022"


def test_supprime_espaces_excessifs_false():
    mot = supprime_espaces_excessifs("Octobre   31,  2022  ")
    assert mot != "Octobre 31, 2022 "


def test_nouveau_mot():
    mot = nouveau_mot("PRédi&ction  ")
    assert mot == "prediction"


def test_nouveau_mot_false():
    mot = nouveau_mot("PRédi&ction  ")
    assert mot != "pRediction "


def test_ratio_similarite():
    ratio = ratio_similarite("New-Or . ls", "New Orleans")
    assert ratio == 0.7619047619047619


def test_ratio_similarite_false():
    ratio = ratio_similarite("New-Or . ls", "New Orleans")
    assert ratio != 0.6


def test_attribution_teams():
    team = attribution_teams(
        "oston Celt",
        0.8,
        ["Boston Celtics", "Miami Heat", "Toronto Raptors", "Phoenix Suns"],
    )
    assert team == "Boston Celtics"


def test_attribution_teams_aucune_ressemblance():
    team = attribution_teams(
        "oston t",
        0.8,
        ["Boston Celtics", "Miami Heat", "Toronto Raptors", "Phoenix Suns"],
    )
    assert team == False
