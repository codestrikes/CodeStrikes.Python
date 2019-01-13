from sdk.area import Area
from sdk.roundContext import RoundContext


class PlayerBot:
    def __init__(self):
        self._attack1 = Area.HookKick
        self._attack2 = Area.HookPunch
        self._defence = Area.HookKick
        self._myScoreTotal = 0
        self._opponentScoreTotal = 0

    def next_move(self, context: RoundContext):
        self._myScoreTotal += context.my_damage
        self._opponentScoreTotal += context.opponent_damage

        context.my_moves.add_attack(self._attack1)
        context.my_moves.add_attack(self._attack2)
        context.my_moves.add_defence(self._defence)

        return context.my_moves

    def __str__(self):
        return "Player Bot"
