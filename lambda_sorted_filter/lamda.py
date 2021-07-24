
numero: int = 1 # variable de tipo int
cadena: str = "hola" # variable de tipo string
diccionario: Dict[str, str] = {"hola": "adios"} # variable de tipo dict

funcion: Callable[[Any], Any] = lambda x: x  # variable de tipo function
def function(x):
    return x

function(1) # -> 1

suma = lambda x, y: x + y
resta = lambda x, y: x - y

def operacion(x: int, y: int, func: Callable[[int, int], int]) -> int:
    return func(x, y)

players = sorted(players, key=lambda x: x['team']['id'])
def get_player_key(player: Dict[str, Any]) -> int:
    return player['team']['id']
def get_player_team_id(player: Dict[str, Any]) -> int:
    return player['team']['id']
players = sorted(players, key=get_player_team_id)

players = [
    {
        "first_name":"LeBron",
        "team":{
          "id":14,
        }
    },
    {
        "first_name":"Pepe",
        "team":{
          "id":100,
        }
    },
    {
        "first_name":"Manolo",
        "team":{
          "id":1,
        }
    }
]

suma = lambda x, y: x + y
suma2 = partial(suma, y=2)
def suma2(x: int) -> int:
    return suma(x, 2)

suma2(5)
