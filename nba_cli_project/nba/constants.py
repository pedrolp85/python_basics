from enum import Enum

VERSION = "0.0.1"


class PlayerOrder(str, Enum):
    TEAM_ID = "team_id"
    PLAYER_ID = "player_id"
    TEAM_NAME = "team_name"
    PLAYER_NAME = "player_name"
    NONE = "no_order"


class Conference(str, Enum):
    EAST = "east"
    WEST = "west"
    ALL = "all"
