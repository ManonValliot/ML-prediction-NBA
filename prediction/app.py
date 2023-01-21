from __future__ import annotations

import asyncio
from prediction.lib_predictions import prediction, proba
from prediction.lib_levenshtein import attribution_teams
from rich.markdown import Markdown
from textual.app import App, ComposeResult
from textual.containers import Content
from textual.widgets import Static, Input, Footer, Label, Header
from textual.containers import Horizontal


TEAMS = [
    "Indiana Pacers",
    "Orlando Magic",
    "Toronto Raptors",
    "Atlanta Hawks",
    "Boston Celtics",
    "Miami Heat",
    "Memphis Grizzlies",
    "San Antonio Spurs",
    "Chicago Bulls",
    "Denver Nuggets",
    "Phoenix Suns",
    "Golden State Warriors",
    "Los Angeles Lakers",
    "Charlotte Bobcats",
    "Washington Wizards",
    "Detroit Pistons",
    "New York Knicks",
    "Houston Rockets",
    "Milwaukee Bucks",
    "Utah Jazz",
    "Portland Trail Blazers",
    "Los Angeles Clippers",
    "Philadelphia 76ers",
    "New Orleans/Oklahoma City Hornets",
    "Seattle SuperSonics",
    "Dallas Mavericks",
    "Sacramento Kings",
    "Cleveland Cavaliers",
    "New Jersey Nets",
    "Minnesota Timberwolves",
    "New Orleans Hornets",
    "Oklahoma City Thunder",
    "Brooklyn Nets",
    "New Orleans Pelicans",
    "Charlotte Hornets",
]


class CustomFooter(Footer):
    """Customisation du pied de page."""

    def compose(self) -> ComposeResult:
        yield Horizontal(
            Label(Markdown(f"Quitter : ctrl+c")),
        )


class MyApp(App):
    """Prédit l'issue d'un match de saison régulière de NBA."""

    CSS_PATH = "app.css"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.team_home = Input(
            id="team_home", placeholder="Entrer l'équipe à domicile..."
        )
        self.team_visitor = Input(
            id="team_visitor", placeholder="Entrer l'équipe à l'extérieur..."
        )

    def compose(self) -> ComposeResult:
        yield Static(Markdown(f"# Prédiction sur un match de saison régulière de NBA"))
        yield self.team_home
        yield self.team_visitor
        yield Content(
            Static(
                Markdown(
                    f" _Veuillez entrer les deux équipes pour que la prédiction sur l'issue du match se lance._"
                ),
                id="results",
            ),
            id="results-container",
        )
        yield CustomFooter()

    def on_mount(self) -> None:
        """Applique le focus sur le premier input, à l'ouverture de l'application, pour que nous puissions commencer à taper tout de suite."""
        self.query_one("#team_home", Input).focus()

    async def on_input_changed(self) -> None:
        """Lance la prédiction si les deux équipes sont indiquées, sinon nettoi la zone de résultat."""
        if self.team_home.value and self.team_visitor.value:
            team_home = attribution_teams(self.team_home.value, 0.75, TEAMS)
            team_visitor = attribution_teams(self.team_visitor.value, 0.75, TEAMS)
            if team_home == False or team_visitor == False:
                self.query_one("#results", Static).update(
                    Markdown(f" _Veuillez entrer des noms d'équipes corrects._")
                )
            else:
                asyncio.create_task(self.predict(team_home, team_visitor))
        else:
            self.query_one("#results", Static).update(
                Markdown(
                    f" _Veuillez entrer les deux équipes pour que la prédiction sur l'issue du match se lance._"
                )
            )

    async def predict(self, home: str, visitor: str) -> None:
        """Applique la prédiction."""
        predict = str(prediction("data.csv", home, visitor)[0])
        proba_home = proba("data.csv", home, visitor)[0]
        proba_visitor = proba("data.csv", home, visitor)[1]
        markdown = self.make_markdown(predict, home, visitor, proba_home, proba_visitor)
        self.query_one("#results", Static).update(Markdown(markdown))

    def make_markdown(
        self, predict: int, home: str, visitor: str, proba_h: float, proba_v: float
    ) -> str:
        """Convertit le résultat en markdown."""
        lines = []
        lines.append(f" _Le report :_")
        chaine = "L'équipe à domicile est : " + home
        lines.append(f" - {chaine}")
        lines.append(" ")
        chaine2 = "L'équipe à l'extérieur est : " + visitor
        lines.append(f" - {chaine2}")
        if predict == 1:
            issue = home
        else:
            issue = visitor
        lines.append(f" _Le résultat :_")
        lines.append(f" - Le résultat est : {issue} gagne!")
        lines.append(f" _Les probabiltés estimées du modèle :_")
        lines.append(f" - {home} perd et que {visitor} gagne : {round(proba_h, 3)}")
        lines.append(f" - {home} gagne et que {visitor} perd : {round(proba_v, 3)}")
        return "\n\n".join(lines)


if __name__ == "__main__":
    app = MyApp()
    app.run()
