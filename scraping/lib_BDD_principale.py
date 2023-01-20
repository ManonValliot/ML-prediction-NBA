"""Description.

Librairie qui construit une base de données à partir des résultats des matchs de NBA sur le site Basketball-Referance.
Ces données représentent les informations principales : la date du match, les équipes en jeu et leur points associés.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class BDD_principale:
    """Création de l'objet base de données principale."""

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.BDD = pd.DataFrame()

    def __repr__(self):
        """
        >>> repr(BDD_principale(pd.DataFrame()))
        'BDD_principale(BDD=Empty DataFrame\nColumns: []\nIndex: [])'
        """
        return f"BDD_principale(BDD={repr(self.BDD)})"

    def creation_BDD(self) -> pd.DataFrame:
        """Retourne une base de données avec les informations principale."""
        Date = self.driver.find_elements(By.XPATH, '//*[@id="schedule"]/tbody/tr/th/a')
        Team_Visitor = self.driver.find_elements(
            By.XPATH, '//*[@id="schedule"]/tbody/tr/td[2]/a'
        )
        Team_Home = self.driver.find_elements(
            By.XPATH, '//*[@id="schedule"]/tbody/tr/td[4]/a'
        )
        Points_Visitor = self.driver.find_elements(
            By.XPATH, '//*[@id="schedule"]/tbody/tr/td[3]'
        )
        Points_Home = self.driver.find_elements(
            By.XPATH, '//*[@id="schedule"]/tbody/tr/td[5]'
        )

        if len(Team_Visitor) == 0:
            Team_Visitor = self.driver.find_elements(
                By.XPATH, '//*[@id="schedule"]/tbody/tr/td[1]/a'
            )
        else:
            Team_Visitor = Team_Visitor

        if len(Team_Home) == 0:
            Team_Home = self.driver.find_elements(
                By.XPATH, '//*[@id="schedule"]/tbody/tr/td[3]/a'
            )
        else:
            Team_Home = Team_Home

        if len(Points_Visitor) == 0:
            Points_Visitor = self.driver.find_elements(
                By.XPATH, '//*[@id="schedule"]/tbody/tr/td[2]'
            )
        else:
            Points_Visitor = Points_Visitor

        if len(Points_Home) == 0:
            Points_Home = self.driver.find_elements(
                By.XPATH, '//*[@id="schedule"]/tbody/tr/td[4]'
            )
        else:
            Points_Home = Points_Home

        liste_Date = []
        liste_Team_Home = []
        liste_Team_Visitor = []
        liste_Points_Visitor = []
        liste_Points_Home = []

        for i in range(len(Date)):
            liste_Date.append(Date[i].text[-12:])
            liste_Team_Visitor.append(Team_Visitor[i].text)
            liste_Team_Home.append(Team_Home[i].text)
            liste_Points_Visitor.append(Points_Visitor[i].text)
            liste_Points_Home.append(Points_Home[i].text)

        self.BDD["Date"] = liste_Date
        self.BDD["Team_Home"] = liste_Team_Home
        self.BDD["Team_Visitor"] = liste_Team_Visitor
        self.BDD["Points_Visitor"] = liste_Points_Visitor
        self.BDD["Points_Home"] = liste_Points_Home

        return self.BDD
