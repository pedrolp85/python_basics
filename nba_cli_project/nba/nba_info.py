from abc import ABCMeta, abstractmethod
import requests

class NBAInfo(metaclass=ABCMeta):


    @abstractmethod
    def get_players(self):
        pass
    
    @abstractmethod
    def get_teams(self,conference: str):
        pass


class NBAInfoMock(NBAInfo):

    def get_players(self):
        return [
            {
                'first_name': 'Pedro', 
                'last_name': 'Garcia'
            },
            {
                'first_name': 'Manolo', 
                'last_name': 'Garcia'
            }
        ]
    
    def get_teams(self, conference: str):
        return [
            {
                'full_name': 'equipo1',
            },
            {
                'full_name': 'equipo2',
            },
        ]

class NBAInfoApi(NBAInfo):

    URL = 'https://www.balldontlie.io/api/'
    API_VERSION = 'v1'
    
    def get_players(self):
        r = requests.get(f"{self.URL}{self.API_VERSION}/players")
        return r.json()['data']
    
    def get_teams(self, conference: str):
        r = requests.get(f"{self.URL}{self.API_VERSION}/teams")
        conference = conference.capitalize()
        teams = []
        for team in r.json()['data']:
            if conference == 'All' or team['conference'] == conference:
                teams.append(team)
        return teams


class NBAInfoDataBase(NBAInfo):

    def get_players(self):
        pass
    
    def get_teams(self, conference: str):
        pass


def get_nba_info() -> NBAInfo:
    return NBAInfoApi()