from abc import ABCMeta, 
from typing import List, Dict, Any, Optional

class PrintOutput(metaclass = ABCMeta):

    @abstractmethod
    def print_output(self, players: List[dict] , output: str, order_by: str):
        pass

    @abstractmethod
    def output_data_modifiers(self, players: List[Dict[str, Any]] , output: str, order_by: str, filter_by: str, num_players: int) -> List[Dict[str, Any]]:
        pass 

class PrintOutputApi(PrintOutput):

    def output_data_modifiers(self, players: List[Dict[str, Any]] , order_by: str, filter_by: str, num_players: int) -> List[Dict[str, Any]]:
        
        new_players = copy.deepcopy(players)
        
        if order_by == 'team_id':
            new_players = sorted(players, key=lambda x: x['team']['id'])
        
        if order_by == 'player_id':
            new_players = sorted(players, key=lambda x: x['id'])

        if order_by == 'player_name':
            new_players = sorted(players, key=lambda x: x['Last_name'])
        
        if ordery_by == 'player_name':
            new_players = sorted(players, key=lambda x: x['team']['full_name'])

        return new_players
    
    def print_output_stream(self, players: List[Dict[str, Any]] , output: str) -> None:
                   
        if output == 'stdout':
            
            print(f"These are the first {len(players)} players on the Roster")
            for player in players:
                print(f"{player['first_name']} {player['last_name']} plays for the {player['team']['full_name']}")
        else:
            
            path = f"tmp/{output}"
            f = open(path, 'w+')
            f.write(f"These are the first {len(players)} players on the Roster\n")
            for player in players:
                f.write(f"{player['first_name']} {player['last_name']} plays for the {player['team']['full_name']}\n")
            
            f.close()

def output_options() -> PrintOutput:
    return PrintOutputApi()