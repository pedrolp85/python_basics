import typer
import requests
from nba.constants import VERSION
from nba.nba_info import get_nba_info
from enum import Enum

class Conference(str, Enum):
    EAST = 'east'
    WEST = 'west'
    ALL = 'all'


app = typer.Typer()


@app.command()
def players():
    print (f"nbacli version {VERSION}")
    nba_info = get_nba_info()
    players = nba_info.get_players()
    print(f"These are the first {len(players)} players on the Roster")
    for player in players:
        print(f"{player['first_name']} {player['last_name']}")

@app.command()       
def teams(conference: Conference = typer.Option(Conference.ALL)):
    print (f"nbacli version {VERSION}")
    
    nba_info = get_nba_info()
    teams = nba_info.get_teams(conference.value)
    print(f"Thes are the first {len(teams)} teams on the League")
    for team in teams:
        print(f"{team['full_name']}")



@app.command()
def match():
    print("")


if __name__ == "__main__":
    app()