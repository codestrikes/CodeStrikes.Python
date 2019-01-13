from sdk.moveCollection import MoveCollection


class RoundContext:
    def __init__(self,
                 last_opponent_moves: MoveCollection,
                 my_damage: int,
                 opponent_damage: int,
                 my_life_points: int,
                 opponent_life_points: int):
        self._lastOpponentMoves = last_opponent_moves
        self._myDamage = my_damage
        self._opponentDamage = opponent_damage
        self._myMoves = MoveCollection()
        self._myLifePoints = my_life_points
        self._opponentLifePoints = opponent_life_points

    def set_moves(self, moves: MoveCollection) -> None:
        self._myMoves = moves

    @property
    def my_moves(self) -> MoveCollection:
        return self._myMoves

    @property
    def last_opponent_moves(self) -> MoveCollection:
        return self._lastOpponentMoves

    @property
    def my_damage(self) -> int:
        return self._myDamage

    @property
    def opponent_damage(self) -> int:
        return self._opponentDamage
