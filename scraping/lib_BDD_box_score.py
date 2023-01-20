"""Description.

Librairie qui construit une base de données à partir des résultats des matchs de NBA sur le site Basketball-Referance.
Ces données représentent des informations complémentaires sur les matchs, comme le nombre de rebonds, etc. 
On récupère ces informations dans un hyperlien, nommé "box score", présent pour chaque match du tableau initial.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


class BDD_box_score:
    """Création de l'objet base de données box score."""

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.BDD = pd.DataFrame()

    def __repr__(self):
        """
        >>> repr(BDD_box_score(pd.DataFrame()))
        'BDD_box_score(BDD=Empty DataFrame\nColumns: []\nIndex: [])'
        """
        return f"BDD_box_score(BDD={repr(self.BDD)})"

    def creation_BDD(self) -> pd.DataFrame:
        """Retourne une base de données avec les informations secondaires."""
        Team_V = self.driver.find_element(
            By.XPATH, '//*[@id="line_score"]/tbody/tr[1]/th/a'
        ).text
        Team_H = self.driver.find_element(
            By.XPATH, '//*[@id="line_score"]/tbody/tr[2]/th/a'
        ).text
        Date = self.driver.find_element(By.XPATH, '//*[@id="inner_nav"]/ul/li[1]/a/u')
        Team_Visitor = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[2]/div[1]/div[1]/strong/a'
        )
        Team_Home = self.driver.find_element(
            By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/strong/a'
        )
        Field_Goals_Made_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[2]'.format(Team_V)
        )
        Field_Goals_Attempted_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[3]'.format(Team_V)
        )
        Field_Goal_Percentage_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[4]'.format(Team_V)
        )
        Three_Point_Field_Goals_Made_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[5]'.format(Team_V)
        )
        Three_Point_Field_Goals_Attempted_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[6]'.format(Team_V)
        )
        Three_Point_Field_Goal_Percentage_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[7]'.format(Team_V)
        )
        Free_Throws_Made_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[8]'.format(Team_V)
        )
        Free_Throws_Attempted_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[9]'.format(Team_V)
        )
        Free_Throw_Percentage_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[10]'.format(Team_V)
        )
        Offensive_Rebounds_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[11]'.format(Team_V)
        )
        Defensive_Rebounds_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[12]'.format(Team_V)
        )
        Rebounds_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[13]'.format(Team_V)
        )
        Assists_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[14]'.format(Team_V)
        )
        Steals_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[15]'.format(Team_V)
        )
        Blocks_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[16]'.format(Team_V)
        )
        Turnovers_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[17]'.format(Team_V)
        )
        Personal_Fouls_V = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[18]'.format(Team_V)
        )
        Field_Goals_Made_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[2]'.format(Team_H)
        )
        Field_Goals_Attempted_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[3]'.format(Team_H)
        )
        Field_Goal_Percentage_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[4]'.format(Team_H)
        )
        Three_Point_Field_Goals_Made_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[5]'.format(Team_H)
        )
        Three_Point_Field_Goals_Attempted_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[6]'.format(Team_H)
        )
        Three_Point_Field_Goal_Percentage_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[7]'.format(Team_H)
        )
        Free_Throws_Made_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[8]'.format(Team_H)
        )
        Free_Throws_Attempted_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[9]'.format(Team_H)
        )
        Free_Throw_Percentage_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[10]'.format(Team_H)
        )
        Offensive_Rebounds_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[11]'.format(Team_H)
        )
        Defensive_Rebounds_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[12]'.format(Team_H)
        )
        Rebounds_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[13]'.format(Team_H)
        )
        Assists_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[14]'.format(Team_H)
        )
        Steals_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[15]'.format(Team_H)
        )
        Blocks_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[16]'.format(Team_H)
        )
        Turnovers_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[17]'.format(Team_H)
        )
        Personal_Fouls_H = self.driver.find_element(
            By.XPATH, '//*[@id="box-{}-game-basic"]/tfoot/tr/td[18]'.format(Team_H)
        )

        self.BDD["Date"] = [Date.text[:12]]
        self.BDD["Team_Visitor"] = [Team_Visitor.text]
        self.BDD["Team_Home"] = [Team_Home.text]
        self.BDD["Field_Goals_Made_V"] = [Field_Goals_Made_V.text]
        self.BDD["Field_Goals_Attempted_V"] = [Field_Goals_Attempted_V.text]
        self.BDD["Field_Goal_Percentage_V"] = [Field_Goal_Percentage_V.text]
        self.BDD["Three_Point_Field_Goals_Made_V"] = [
            Three_Point_Field_Goals_Made_V.text
        ]
        self.BDD["Three_Point_Field_Goals_Attempted_V"] = [
            Three_Point_Field_Goals_Attempted_V.text
        ]
        self.BDD["Three_Point_Field_Goal_Percentage_V"] = [
            Three_Point_Field_Goal_Percentage_V.text
        ]
        self.BDD["Free_Throws_Made_V"] = [Free_Throws_Made_V.text]
        self.BDD["Free_Throws_Attempted_V"] = [Free_Throws_Attempted_V.text]
        self.BDD["Free_Throw_Percentage_V"] = [Free_Throw_Percentage_V.text]
        self.BDD["Offensive_Rebounds_V"] = [Offensive_Rebounds_V.text]
        self.BDD["Defensive_Rebounds_V"] = [Defensive_Rebounds_V.text]
        self.BDD["Rebounds_V"] = [Rebounds_V.text]
        self.BDD["Assists_V"] = [Assists_V.text]
        self.BDD["Steals_V"] = [Steals_V.text]
        self.BDD["Blocks_V"] = [Blocks_V.text]
        self.BDD["Turnovers_V"] = [Turnovers_V.text]
        self.BDD["Personal_Fouls_V"] = [Personal_Fouls_V.text]
        self.BDD["Field_Goals_Made_H"] = [Field_Goals_Made_H.text]
        self.BDD["Field_Goals_Attempted_H"] = [Field_Goals_Attempted_H.text]
        self.BDD["Field_Goal_Percentage_H"] = [Field_Goal_Percentage_H.text]
        self.BDD["Three_Point_Field_Goals_Made_H"] = [
            Three_Point_Field_Goals_Made_H.text
        ]
        self.BDD["Three_Point_Field_Goals_Attempted_H"] = [
            Three_Point_Field_Goals_Attempted_H.text
        ]
        self.BDD["Three_Point_Field_Goal_Percentage_H"] = [
            Three_Point_Field_Goal_Percentage_H.text
        ]
        self.BDD["Free_Throws_Made_H"] = [Free_Throws_Made_H.text]
        self.BDD["Free_Throws_Attempted_H"] = [Free_Throws_Attempted_H.text]
        self.BDD["Free_Throw_Percentage_H"] = [Free_Throw_Percentage_H.text]
        self.BDD["Offensive_Rebounds_H"] = [Offensive_Rebounds_H.text]
        self.BDD["Defensive_Rebounds_H"] = [Defensive_Rebounds_H.text]
        self.BDD["Rebounds_H"] = [Rebounds_H.text]
        self.BDD["Assists_H"] = [Assists_H.text]
        self.BDD["Steals_H"] = [Steals_H.text]
        self.BDD["Blocks_H"] = [Blocks_H.text]
        self.BDD["Turnovers_H"] = [Turnovers_H.text]
        self.BDD["Personal_Fouls_H"] = [Personal_Fouls_H.text]

        return self.BDD
