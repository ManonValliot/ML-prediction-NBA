"""
Description.

Librairie qui utilise l'algorithme de Levenshtein pour trouver le nom d'équipe le plus semblable.
"""

import unidecode
import Levenshtein as lev


def minuscule(mot: str) -> str:
    """Retourne le mot en minuscule.

    Exemple :
    >>> minuscule('CHaPeau')
    'chapeau'
    """
    mot = mot.lower()
    return mot


def supprime_caracteres(mot: str) -> str:
    """Supprime les cartaères d'un mot.

    Exemple :
    >>> supprime_caracteres('informa&tique%')
    'informatique'
    """
    carateres = "1234567890&'(!)_°@#^¨$*€`£%=+:;.,?"
    for caratere in carateres:
        mot = mot.replace(caratere, "")
    return mot


def enleve_accents(mot: str) -> str:
    """Enlève les accents d'un mot.

    Exemple :
    >>> enleve_accents('prédiction')
    'prediction'
    """
    mot = unidecode.unidecode(mot)
    return mot


def remplace_tiret(mot: str) -> str:
    """Remplace les tirets d'un mot par un espace.

    Exemple :
    >>> remplace_tiret('New-Orleans')
    'New Orleans'
    """
    mot = mot.replace("-", " ")
    return mot


def supprime_espaces_excessifs(mot: str) -> str:
    """Supprime les espaces inutiles danns le mot.

    Exemple :
    >>> supprime_espaces_excessifs('Octobre   31,  2022  ')
    'Octobre 31, 2022'
    """
    mot = " ".join(mot.split())
    return mot


def nouveau_mot(mot: str) -> str:
    """Applique toutes les transformations précédentes à notre mot.

    Exemple :
    >>> nouveau_mot('PRédi&ction  ')
    'prediction'
    """
    mot = minuscule(mot)
    mot = supprime_espaces_excessifs(mot)
    mot = enleve_accents(mot)
    mot = remplace_tiret(mot)
    mot = supprime_caracteres(mot)
    return mot


def ratio_similarite(mot_compare: str, mot_comparaison: str) -> float:
    """Calcule la similarité entre deux mots (algorithme de Levenshtein).
    Notre mot_comparaison peut être ecrit avec des accents, des majuscules et des tirets.

    Exemple :
    >>> ratio_similarite('New-Or . ls', 'New Orleans')
    0.7619047619047619
    """
    mot_compare = nouveau_mot(mot_compare)
    mot_comparaison = remplace_tiret(mot_comparaison)
    Ratio = lev.ratio(mot_compare, unidecode.unidecode(mot_comparaison.lower()))
    return Ratio


def attribution_teams(mot_compare: str, ratio: float, liste_teams: list[str]) -> str:
    """Attribut les bons noms d'équipe.

    Exemple :
    >>> attribution_teams('oston Celt', 0.8, ["Boston Celtics", "Miami Heat", "Toronto Raptors", "Phoenix Suns"])
    'Boston Celtics'
    """
    liste_ratio = []
    for team in liste_teams:
        liste_ratio.append(ratio_similarite(mot_compare, minuscule(team)))
    if max(liste_ratio) >= ratio:
        index = liste_ratio.index(max(liste_ratio))
        return liste_teams[index]
    else:
        return False
