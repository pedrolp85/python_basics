import sys
from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List, Optional

import requests

from nba.constants import Conference, PlayerOrder

# Un concepto importante en programación orientada
# a objetos es el de las clases abstractas.
# Unas clases en las que se pueden definir tanto métodos como propiedades,
# pero que no pueden ser instancias directamente.
# Solamente se pueden usar para construir subclases.
# Permitiendo así tener una única implementación de los métodos compartidos,
# evitando la duplicación de código.

# Propiedades de las Clases abstractas:
#  1 - No se pueden instanciar directamente
#      Simplemente proporciona una interfaz para las subclases derivadas
#      y evitando así la duplicación de código.

#  2 - No es necesario que implemente todos los métodos
#      Los métodos declarados pueden ser abstractos,
#      pero es necesario que sean implementados
#      en las subclases

#  Para poder crear clases abstractas en Python es necesario importar
#  la clase ABCMeta y el decorador abstractmethod
#  del modulo abc (Abstract Base Classes).

# El ultimo método se llama inyección de dependencias, pendiente de repasarlo


class NBAInfo(metaclass=ABCMeta):
    @abstractmethod
    def get_players(self):
        pass

    @abstractmethod
    def get_teams(self, conference: Conference):
        pass

    @abstractmethod
    def get_match(self, num_matches: int, team: Optional[str] = None):
        pass


class NBAInfoMock(NBAInfo):
    def get_players(self):
        return [
            {"first_name": "Pedro", "last_name": "Garcia"},
            {"first_name": "Manolo", "last_name": "Garcia"},
        ]

    def get_teams(self, conference: str):
        return [
            {
                "full_name": "equipo1",
            },
            {
                "full_name": "equipo2",
            },
        ]


class NBAInfoApi(NBAInfo):

    URL = "https://www.balldontlie.io/api/"
    API_VERSION = "v1"
    PLAYERS_PPAGE = 100
    TEAMS_PPAGE = 30
    MAX_PLAYERS_API_FETCH = 100
    MAX_PLAYERS_AVAILABLES = sys.maxsize * 2 + 1
    MAX_MATCHES_AVAILABLES = sys.maxsize * 2 + 1
    MAX_MATCHES_API_FETCH = 100

    ORDER_BY_PLAYERS = {
        PlayerOrder.TEAM_ID: lambda x: x["team"]["id"],
        PlayerOrder.PLAYER_ID: lambda x: x["id"],
        PlayerOrder.TEAM_NAME: lambda x: x["team"]["full_name"],
        PlayerOrder.PLAYER_NAME: lambda x: x["last_name"],
    }

    # Este método lo van a usar los métodos get_players
    # y get_matches internamente, no tiene sentido que
    # lo use un cliente de la librería
    # con _nombre indicamos que es un método protegido,
    # que no se toque desde una instancia externa
    # con __nombre indicamos que es private, la diferencia
    # es que las subclases no podrían acceder a él

    def _fetch_from_api(
        self, uri_path: str, num_data_fetch: int, max_data_fetch: int
    ) -> List[Dict[str, Any]]:

        data_fetched = []
        current_page = 1
        while num_data_fetch > 0 and current_page is not None:
            data_to_request = (
                max_data_fetch if num_data_fetch > max_data_fetch else num_data_fetch
            )
            r = requests.get(
                f"{self.URL}{self.API_VERSION}/{uri_path}?"
                f"per_page={max_data_fetch}&page={current_page}"
            )
            new_data_fetched = r.json()["data"][:data_to_request]
            data_fetched.extend(new_data_fetched)
            current_page = r.json()["meta"]["next_page"]
            num_data_fetch -= data_to_request

        return data_fetched

    def get_players(
        self,
        num_players: int,
        team: Optional[str] = None,
        order_by: Optional[PlayerOrder] = None,
    ) -> List[Dict[str, Any]]:

        players = []

        num_fetch_players = (
            num_players
            if (num_players > 0 and team is None)
            else self.MAX_PLAYERS_AVAILABLES
        )
        players = self._fetch_from_api(
            "players", num_fetch_players, self.MAX_PLAYERS_API_FETCH
        )
        if team is not None:
            players = [player for player in players if player["team"]["name"] == team]

        if order_by != PlayerOrder.NONE:
            players = sorted(players, key=self.ORDER_BY_PLAYERS[order_by])

        if num_players < len(players) and team is not None:
            players = players[:num_players]

        return players

    def get_teams(self, conference: Conference):

        r = requests.get(f"{self.URL}{self.API_VERSION}/teams")
        conference = conference.capitalize()
        teams = []
        for team in r.json()["data"]:
            if conference == "All" or team["conference"] == conference:
                teams.append(team)
        return teams

    def get_match(
        self, num_matches: int, team: Optional[str] = None
    ) -> List[Dict[str, Any]]:

        matches = []

        num_matches_fetch = (
            num_matches
            if (num_matches > 0 and team is None)
            else self.MAX_MATCHES_AVAILABLES
        )
        matches = self._fetch_from_api(
            "games", num_matches_fetch, self.MAX_MATCHES_API_FETCH
        )
        if team is not None:
            matches = [
                match
                for match in matches
                if (
                    match["home_team"]["name"] == team
                    or match["visitor_team"]["name"] == team
                )
            ]

        return matches


class NBAInfoDataBase(NBAInfo):
    def get_players(self):
        pass

    def get_teams(self, conference: str):
        pass


# Esto es inyección de dependencias


def get_nba_info() -> NBAInfo:
    return NBAInfoApi()
