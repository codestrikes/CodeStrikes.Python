import random as randomImport
from sdk.area import Area
from sdk.roundContext import RoundContext


class Kickboxer:
    def __init__(self):
        self._attack1 = Area.HookKick
        self._defence = Area.HookKick

    def create_random_attack(self):
        rnd = randomImport.random()
        if rnd < 0.3:
            return Area.HookKick
        if rnd < 0.7:
            return Area.HookPunch
        if rnd < 0.9:
            return Area.LowKick

        return Area.LowKick

    def next_move(self, context: RoundContext):
        if (context.last_opponent_moves is not None) and not context.last_opponent_moves.has_defence(self._attack1):
            self._attack1 = self.create_random_attack()
        attack2 = self.create_random_attack()

        context.my_moves.add_attack(self._attack1)
        context.my_moves.add_attack(attack2)
        context.my_moves.add_defence(self._defence)

        return context.my_moves

    def __str__(self):
        return "Kickboxer"
