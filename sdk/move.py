from sdk.area import Area
from sdk.moveType import MoveType


class Move:
    def __init__(self, move_type, area):
        self._moveType = move_type
        self._area = area

    @property
    def area(self) -> Area:
        return self._area

    @property
    def move_type(self) -> MoveType:
        return self._moveType

    @property
    def attack_power(self) -> int:
        switcher = {
            Area.HookKick: 16,
            Area.HookPunch: 6,
            Area.UppercutPunch: 3,
            Area.LowKick: 1
        }

        return switcher.get(self._area, 0)

    def energy(self) -> int:
        if self._moveType == MoveType.Defense:
            return 0

        switcher = {
            Area.HookKick: 4,
            Area.HookPunch: 3,
            Area.UppercutPunch: 2,
            Area.LowKick: 1
        }
        return switcher.get(self._area, 0)
