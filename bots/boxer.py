import random as randomImport
from sdk.area import Area
from sdk.roundContext import RoundContext


class Boxer:
    def __init__(self):
        self._attack1 = Area.HookKick
        self._attack2 = Area.HookPunch
        self._defence = Area.HookKick
        self._myScoreTotal = 0
        self._opponentScoreTotal = 0

    def change_defence(self, old_defence: Area) -> Area:
        if old_defence == Area.HookKick:
            return Area.HookPunch
        return Area.HookKick

    def create_random_attack(self):
        if randomImport.random() > 0.5:
            return Area.LowKick
        return Area.HookPunch

    def next_move(self, context: RoundContext):
        self._myScoreTotal += context.my_damage
        self._opponentScoreTotal += context.opponent_damage

        context.my_moves.add_attack(self._attack1)
        context.my_moves.add_attack(self._attack2)

        if (context.last_opponent_moves is not None) and not context.last_opponent_moves.has_attack(self._defence):
            self._defence = self.change_defence(self._defence)

        if self._myScoreTotal >= self._opponentScoreTotal:
            context.my_moves.add_attack(self.create_random_attack())
        else:
            context.my_moves.add_defence(self._defence)

        return context.my_moves

    def __str__(self):
        return "Boxer"
