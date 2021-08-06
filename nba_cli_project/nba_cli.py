from enum import Enum

import requests
import typer

from nba.constants import VERSION, Conference, PlayerOrder
from nba.nba_info import get_nba_info
from output.output_options import output_options

# Estándar para imports: (separados por linea en blanco)
# Libreria estándar arriba

# librarias no estándar en medio

# imports de código abajo


app = typer.Typer()

# Ejercicios: Pasar las funciones de print output y orderby a otra interfaz
# hacer Filterby con list_comprehension y filter()
# implementar matches igual que players
# hacer que get_players tenga un parametro team opcional, que nos obtiene todos los de un equipo


@app.command()
def players(
    n: int = typer.Option(25),
    team: str = typer.Option(None),
    all: bool = typer.Option(False),
    output: str = typer.Option("stdout"),
    order_by: PlayerOrder = typer.Option(PlayerOrder.NONE),
):

    print(f"\nbacli version {VERSION}\n")
    nba_info = get_nba_info()
    nba_output = output_options()

    num_players = -1 if all else n

    players = nba_info.get_players(num_players, team, order_by)
    # nba_output.print_players_output_stream(players, output)
    nba_output.send(
        players, [["last_name"], ["first_name"], ["team", "full_name"], ["team", "id"]]
    )


# si escribo "nba_cli players" me muestra los 25 primeros jugadores
# si escribo "nba_cli players --n 50" me muestra los 50 primeros
# si escribo "nba_cli players --all" me muestra todos
# si escribo "nba_cli players --team Lakers" me muestra los jugadores de los lakers
# Otros parámetros: --output [fichero .txt|stdout]
#                   --order-by [team_id|player_id|team_name|player_name|no_order]


@app.command()
def teams(conference: Conference = typer.Option(Conference.ALL)):
    
    print(f"nbacli version {VERSION}")

    nba_info = get_nba_info()
    nba_output = output_options()
    teams = nba_info.get_teams(conference.value)

    print(f"Thes are the first {len(teams)} teams on the League")
    nba_output.send(teams, [["full_name"]])


@app.command()
def matches(
    n: int = typer.Option(25),
    team: str = typer.Option(None),
    all: bool = typer.Option(False),
    output: str = typer.Option("stdout"),
):
    print(f"nbacli version {VERSION}")

    nba_info = get_nba_info()
    nba_output = output_options()

    num_matches = -1 if all else n

    players = nba_info.get_match(num_matches, team)
    nba_output.print_matches_output_stream(players, output)


if __name__ == "__main__":
    app()
