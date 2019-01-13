from typing import Iterable
from sdk.moveType import MoveType
from sdk.move import Move
from sdk.area import Area


class ReadonlyMoveCollection:
    def __init__(self):
        self._moveList = list()

    @property
    def moves(self) -> Iterable[Move]:
        return self._moveList

    @property
    def attacks(self)  -> Iterable[Move]:
        for move in self._moveList:
            if move.move_type == MoveType.Attack:
                yield move

    @property
    def defences(self) -> Iterable[Move]:
        for move in self._moveList:
            if move.move_type == MoveType.Defense:
                yield move

    def has_defence(self, area: Area) -> bool:
        for defence in self.defences:
            if defence.area == area:
                return True
        return False

    def has_attack(self, area: Area) -> bool:
        for defence in self.attacks:
            if defence.area == area:
                return True
        return False

    def sum_energy(self) -> int:
        energy = 0
        for move in self._moveList:
            energy += move.energy()
        return energy
