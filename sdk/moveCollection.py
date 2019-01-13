from sdk.moveType import MoveType
from sdk.move import Move
from sdk.readonlyMoveCollection import ReadonlyMoveCollection
from sdk.area import Area


class MoveCollection(ReadonlyMoveCollection):
    def __init__(self):
        super(MoveCollection, self).__init__()

    def add_attack(self, area: Area):
        move = Move(MoveType.Attack, area)
        self._moveList.append(move)
        return self

    def add_defence(self, area: Area):
        move = Move(MoveType.Defense, area)
        self._moveList.append(move)
        return self
