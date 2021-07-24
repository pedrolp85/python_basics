import typer
import requests
from nba.constants import VERSION
from nba.nba_info import get_nba_info
from print_output.output_options import output_options
from enum import Enum

class Conference(str, Enum):
    EAST = 'east'
    WEST = 'west'
    ALL = 'all'

class Order_param(str, Enum):
    TEAM_ID = 'team_id'
    PLAYER_ID = 'player_id'
    TEAM_NAME = 'team_name'
    PLAYER_NAME = 'player_name'
    NONE = 'no_order'

app = typer.Typer()

# Ejercicios: Pasar las funciones de print output y orderby a otra interfaz
# hacer Filterby con list_comprehension y filter()
# implementar matches igual que players
# hacer que get_players tenga un parametro team opcional, que nos obtiene todos los de un equipo

@app.command()
def players(n: int = typer.Option(25), team: str = typer.Option(None), all: bool = typer.Option(False), output: str = typer.Option('stdout'), order_by: Order_param = typer.Option(Order_param.NONE)):
    print (f"\nbacli version {VERSION}\n")
    nba_info = get_nba_info()
    nba_output = output_options()
    num_players = (
            -1 if all or team is not None 
            else n
        )
    
    if team is not None:
        
        if order_by != 'no_order':
            players = nba_info.get_players_2(num_players, team, order_by)
        else: 
            players = nba_info.get_players_2(num_players, team)
    else:
        players = nba_info.get_players_2(num_players)
    
    
   
    
    #nba_output.output_data_modifiers(players, order_by)
    #(self, players: List[Dict[str, Any]] , order_by: str, filter_by: str, num_players: int) 
    nba_output.print_output_stream(players, output)

@app.command()       
def teams(conference: Conference = typer.Option(Conference.ALL)):
    print (f"nbacli version {VERSION}")
    
    nba_info = get_nba_info()
    nba_output = output_options ()
    teams = nba_info.get_teams(conference.value)
    print(f"Thes are the first {len(teams)} teams on the League")
    for team in teams:
        print(f"{team['full_name']}")

# si escribo "nba_cli players" me muestra los 25 primeros jugadores
# si escribo "nba_cli players --n 50" me muestra los 50 primeros
# si escribo "nba_cli players --all" me muestra todos
# si escribo "nba_cli players --team Lakers" me muestra los jugadores de los lakers


@app.command()
def match():
    print("")


if __name__ == "__main__":
    app()