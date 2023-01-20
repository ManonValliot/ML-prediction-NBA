"""Description.

Librairie qui construit un driver et qui l'initialise à partir d'un lien.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time


def _setup(url):
    """Initialisation du webdriver, mise en place de son setup et lancement de la page."""
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    website = url
    driver.get(website)
    driver.maximize_window()
    return driver


def _cookies(driver):
    """Accepte les cookies s'ils sont demandés, sinon pass."""
    try:
        driver.find_element(By.CLASS_NAME, "css-47sehv").click()
    except:
        pass


class Driver:
    """Création de l'objet driver."""

    def __init__(self, url: str):
        self.url = url

    def __repr__(self) -> str:
        """
        >>> repr(Driver('https://www.basketball-reference.com/leagues/NBA_2020_games.html'))
        "Driver(url='https://www.basketball-reference.com/leagues/NBA_2020_games.html')"
        """
        return f"Driver(url={repr(self.url)})"

    def initialisation(self) -> webdriver:
        """Retourne un webdriver initialisé."""
        driver = _setup(self.url)
        time.sleep(2)
        _cookies(driver)
        time.sleep(1)
        return driver
