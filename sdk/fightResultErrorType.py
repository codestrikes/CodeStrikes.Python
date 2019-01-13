from enum import Enum


class FightResultErrorType(Enum):
    Timeout = 1
    Runtime = 2
    IllegalMove = 3
