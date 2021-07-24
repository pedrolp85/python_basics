from abc import ABCMeta, abstractmethod
import requests
from typing import List, Dict, Any, Optional
import sys

# Un concepto importante en programación orientada a objetos es el de las clases abstractas. 
# Unas clases en las que se pueden definir tanto métodos como propiedades,
# pero que no pueden ser instancias directamente.Solamente se pueden usar para construir subclases. 
# Permitiendo así tener una única implementación de los métodos compartidos, 
# evitando la duplicación de código.

# Propiedades de las Clases abstractas:
#  1 - No se pueden instanciar directamente
#      Simplemente proporciona una interfaz para las subclases derivadas 
#      y evitando así la duplicación de código.

#  2 - No es necesario que implemente todos los métodos
#      Los métodos declarados pueden ser abstractos, pero es necesario que sean implementados
#      en las subclases

#  Para poder crear clases abstractas en Python es necesario importar 
#  la clase ABCMeta y el decorador abstractmethod del modulo abc (Abstract Base Classes). 

# El ultimo método se llama inyección de dependencias, pendiente de repasarlo

class NBAInfo(metaclass=ABCMeta):

    @abstractmethod
    def get_players(self):
        print('hola NBAInfo')
    
    @abstractmethod
    def get_teams(self,conference: str):
        pass
    
    # @abstractmethod
    # def get_match(self, num_matchs: int, team: Optional[str]):
    #     pass


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
    PLAYERS_PPAGE = 100
    TEAMS_PPAGE = 30
    MAX_PLAYERS_API_FETCH = 100
    MAX_PLAYERS_AVAILABLES = sys.maxsize * 2 + 1
    
    def get_players(self,num_players: int):
        
        if num_players > 0:

            last_page_players = num_players % self.PLAYERS_PPAGE
            pages = (
                num_players // self.PLAYERS_PPAGE
                if last_page_players == 0 
                else (num_players // self.PLAYERS_PPAGE)+1
            )
        else: 
            # cogemos todos los jugadores, el número aún no lo sabemos sin hacer
            # la primera consulta a la API
            
            last_page_players = self.PLAYERS_PPAGE
            pages = 1

        players = []
        num_page = 1       
        while (num_page < pages+1):
            print(f"Obteniendo datos...pagina {num_page}")
            retrieve_elements = (
                        last_page_players
                        if (last_page_players !=0 and num_page == pages)
                        else self.PLAYERS_PPAGE
                    )            
            
            try:
                r = requests.get(f"{self.URL}{self.API_VERSION}/players?per_page={self.PLAYERS_PPAGE}&page={num_page}")
                r.raise_for_status()
                
            except requests.exceptions.RequestException as e:
                raise SystemExit(e)
                        
            current_page = r.json()['meta']['current_page']
            next_page = r.json()['meta']['next_page']
            total_players = r.json()['meta']['total_count']
            total_pages = r.json()['meta']['total_pages']
            
            if num_players < 0:
                # La primera vez que entramos aquí num_players es < 0 si --all
                # la segunda iteración no entraremos en ningún caso
                
                num_players = total_players
                last_page_players = num_players % self.PLAYERS_PPAGE
                pages = (
                    num_players // self.PLAYERS_PPAGE
                    if last_page_players == 0 
                    else (num_players // self.PLAYERS_PPAGE)+1
                )
                
            players = players + (r.json()['data'][:retrieve_elements])
            
            if current_page == total_pages:
                print("Hemos obtenido todos los datos, paramos las consultas")
                break

            num_page += 1

        return players
    
    def get_players_2(self, num_players: int, team: Optional[str] = None, order_by: Optional[str]) -> List[Dict[str, Any]]:
        players = []
        remainder_players = num_players if num_players > 0 else self.MAX_PLAYERS_AVAILABLES
        current_page = 1
        while remainder_players > 0 and current_page is not None:
            players_to_request = self.MAX_PLAYERS_API_FETCH if remainder_players > self.MAX_PLAYERS_API_FETCH else remainder_players
            print(f"Leyendo pagina {current_page}, voy a pedir {players_to_request}")
            r = requests.get(f"{self.URL}{self.API_VERSION}/players?per_page={self.MAX_PLAYERS_API_FETCH}&page={current_page}")
            new_players = r.json()['data'][:players_to_request]
            players.extend(new_players)
            print(f"He añadido a mi lista {len(new_players)} nuevos jugadores!")
            current_page = r.json()['meta']['next_page']
            remainder_players -= players_to_request

        return players
    
    def filter_players_byteam(self, players_raw: List[dict], team: str) -> List[dict]:
        # hazme esto mismo con comprension list
        # hazme este mismo llamando a la funcion filter() https://www.programiz.com/python-programming/methods/built-in/filter
        players = []
        for player in players_raw:
            if player['team']['name'] == team:
                players.append(player)
                
        return players


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

# Esto es inyección de dependencias

def get_nba_info() -> NBAInfo:
    return NBAInfoApi()