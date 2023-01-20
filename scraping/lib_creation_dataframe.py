""""Description.

Librairie qui construit un dataframe, sous forme csv, avec les informations, principales et secondaires, 
des résultats des matchs de NBA sur le site Basketball-Referance.
"""

from lib_driver import Driver
from lib_BDD_principale import BDD_principale
from lib_BDD_box_score import BDD_box_score
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd


def longueur_tableau(driver: webdriver) -> int:
    """Fonction qui définie la longueur exacte du tableau.

    Exemple :
    >>> longueur_tableau(Driver('https://www.basketball-reference.com/leagues/NBA_2020_games.html').initialisation())
    71
    """
    liste_titres_tableau = driver.find_elements(
        By.XPATH, '//*[contains(text(),"Home/Neutral")]'
    )
    nombre_titres = len(liste_titres_tableau) - 1
    longueur_tableau = (
        len(driver.find_elements(By.XPATH, '//*[@id="schedule"]/tbody/tr/th/a'))
        + nombre_titres
    )
    return longueur_tableau


def assemblage_BDD_box_score(driver: Driver) -> pd.DataFrame:
    """Assemble toutes les bases de données box score du tableau.

    Exemple :
    >>> assemblage_BDD_box_score(Driver('https://www.basketball-reference.com/leagues/NBA_2008_games-october.html').initialisation())
                Date            Team_Visitor              Team_Home Field_Goals_Made_V Field_Goals_Attempted_V  ... Assists_H Steals_H Blocks_H Turnovers_H Personal_Fouls_H
    0   Oct 30, 2007  Portland Trail Blazers      San Antonio Spurs                 39                      78  ...        21        8        4           8               19
    1   Oct 30, 2007               Utah Jazz  Golden State Warriors                 41                      90  ...        19        8        9          20               28
    2   Oct 30, 2007         Houston Rockets     Los Angeles Lakers                 34                      74  ...        18       16        3          12               22
    3   Oct 31, 2007      Washington Wizards         Indiana Pacers                 36                      99  ...        20       12        6          17               33
    4   Oct 31, 2007         Milwaukee Bucks          Orlando Magic                 33                      87  ...        15        2        9          10               22
    5   Oct 31, 2007      Philadelphia 76ers        Toronto Raptors                 38                      82  ...        23        8        4          10               20
    6   Oct 31, 2007           Chicago Bulls        New Jersey Nets                 38                      96  ...        24        9        7          17               31
    7   Oct 31, 2007        Dallas Mavericks    Cleveland Cavaliers                 33                      69  ...        13       11        2          15               21
    8   Oct 31, 2007       San Antonio Spurs      Memphis Grizzlies                 38                      87  ...        21        5        6          14               19
    9   Oct 31, 2007        Sacramento Kings    New Orleans Hornets                 36                      81  ...        23        6        7          19               24
    10  Oct 31, 2007     Seattle SuperSonics         Denver Nuggets                 40                      96  ...        31       11       10          15               21

    [11 rows x 37 columns]
    """
    df_final = pd.DataFrame()
    for i in range(longueur_tableau(driver)):
        try:
            celulle = driver.find_element(
                By.XPATH, '//*[@id="schedule"]/tbody/tr[{}]/td[6]/a'.format(i + 1)
            )
            lien = celulle.get_attribute("href")
            driver2 = Driver(lien).initialisation()
            df_temporaire = BDD_box_score(driver2).creation_BDD()
            df_final = pd.concat([df_final, df_temporaire])
            driver2.close()
        except:
            try:
                celulle = driver.find_element(
                    By.XPATH, '//*[@id="schedule"]/tbody/tr[{}]/td[5]/a'.format(i + 1)
                )
                lien = celulle.get_attribute("href")
                driver2 = Driver(lien).initialisation()
                df_temporaire = BDD_box_score(driver2).creation_BDD()
                df_final = pd.concat([df_final, df_temporaire])
                driver2.close()
            except:
                pass
    df_final.reset_index(drop=True, inplace=True)
    return df_final


def creation_BDD(driver: Driver, annee_min: int, annee_max: int) -> tuple[pd.DataFrame]:
    """Retourne les bases de données principale et box score sur toutes les années demandées.

    Exemple :
    >>> creation_BDD(Driver, 2007, 2008)
    Output exceeds the size limit. Open the full output data in a text editor
    (          Date            Team_Visitor               Team_Home  Points_Visitor  \
    0  Oct 30, 2007  Portland Trail Blazers       San Antonio Spurs              97   
    1  Oct 30, 2007               Utah Jazz   Golden State Warriors             117   
    2  Oct 30, 2007         Houston Rockets      Los Angeles Lakers              95  
    
      Points_Home
    0         106
    1          96
    2          93 ,
    
                   Date            Team_Visitor            Team_Home   Points_Visitor  \
    0      Oct 30, 2007  Portland Trail Blazers    San Antonio Spurs               97   
    ....
    1312   Jun 15, 2008      Los Angeles Lakers       Boston Celtics               98
    1313   Jun 17, 2008          Boston Celtics   Los Angeles Lakers               92

    [1313 rows x 39 columns])
    """
    df_final_principal = pd.DataFrame()
    df_final_box_score = pd.DataFrame()
    for i in range(annee_min, annee_max):
        url_annee = (
            "https://www.basketball-reference.com/leagues/NBA_{}_games.html".format(
                i + 1
            )
        )
        driver = Driver(url_annee).initialisation()
        nombre_mois = len(
            driver.find_elements(By.XPATH, '//*[@id="content"]/div[2]/div/a')
        )

        for mois in range(nombre_mois):
            url_mois = driver.find_element(
                By.XPATH, '//*[@id="content"]/div[2]/div[{}]/a'.format(mois + 1)
            ).get_attribute("href")
            driver2 = Driver(url_mois).initialisation()
            df_temporaire_principal = BDD_principale(driver2).creation_BDD()
            df_final_principal = pd.concat(
                [df_final_principal, df_temporaire_principal]
            )
            df_temporaire_box_score = assemblage_BDD_box_score(driver2)
            df_final_box_score = pd.concat(
                [df_final_box_score, df_temporaire_box_score]
            )
            driver2.close()
        driver.close()
    df_final_principal.reset_index(drop=True, inplace=True)
    df_final_box_score.reset_index(drop=True, inplace=True)
    return df_final_principal, df_final_box_score


def supprime_espaces_excessifs(mot: str) -> str:
    """Supprime les espaces inutiles dans la chaine de caractères.

    Exemple :
    >>> supprime_espaces_excessifs('  On est  le    17 janvier  ')
    'On est le 17 janvier'
    """
    mot = " ".join(mot.split())
    return mot


def assemblage_BDD(driver: Driver, annee_min: int, annee_max: int) -> pd.DataFrame:
    """Assemble les deux bases de données en fonction des colonnes identiques (date et équipes).

    Exemple :
    >>> assemblage_BDD(Driver, 2007, 2008)
                Date            Team_Visitor              Team_Home  Points_Visitor   Points_Home  ... Assists_H Steals_H Blocks_H Turnovers_H Personal_Fouls_H
    0   Oct 30, 2007  Portland Trail Blazers      San Antonio Spurs              97           106  ...        21        8        4           8               19
    1   Oct 30, 2007               Utah Jazz  Golden State Warriors             117            96  ...        19        8        9          20               28
    2   Oct 30, 2007         Houston Rockets     Los Angeles Lakers              95            93  ...        18       16        3          12               22
    3   Oct 31, 2007      Washington Wizards         Indiana Pacers             110           119  ...        20       12        6          17               33
    4   Oct 31, 2007         Milwaukee Bucks          Orlando Magic              33           102  ...        15        2        9          10               22
    5   Oct 31, 2007      Philadelphia 76ers        Toronto Raptors              83           106  ...        23        8        4          10               20
    6   Oct 31, 2007           Chicago Bulls        New Jersey Nets              97           112  ...        24        9        7          17               31
    7   Oct 31, 2007        Dallas Mavericks    Cleveland Cavaliers             103            74  ...        13       11        2          15               21
    8   Oct 31, 2007       San Antonio Spurs      Memphis Grizzlies              92           101  ...        21        5        6          14               19
    9   Oct 31, 2007        Sacramento Kings    New Orleans Hornets             104           104  ...        23        6        7          19               24
    10  Oct 31, 2007     Seattle SuperSonics         Denver Nuggets             103           120  ...        31       11       10          15               21
    ...

    [1313 rows x 39 columns]
    """
    bases = creation_BDD(driver, annee_min, annee_max)
    for ligne in bases[1]["Date"].index:
        bases[1]["Date"][ligne] = supprime_espaces_excessifs(bases[1]["Date"][ligne])
    for ligne in bases[0]["Date"].index:
        bases[0]["Date"][ligne] = supprime_espaces_excessifs(bases[0]["Date"][ligne])
    df1 = bases[0]
    df2 = bases[1]
    df = pd.merge(df1, df2)
    return df


def conversion_csv(driver: Driver, chemin: str, annee_min: int, annee_max: int):
    """Convertit le dataframe en csv."""
    df = assemblage_BDD(driver, annee_min, annee_max)
    return df.to_csv(chemin, index=False, header=True, sep=";", encoding="utf-8-sig")
