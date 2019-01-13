from sdk.moveCollection import MoveCollection


class RoundResult:
    def __init__(self,
                 round_number: int,
                 player_moves: MoveCollection,
                 opponent_moves: MoveCollection,
                 player_score: int,
                 opponent_score: int):
        self._roundNumber = round_number
        self._playerMoves = player_moves
        self._opponentMoves = opponent_moves
        self._playerScore = player_score
        self._opponentScore = opponent_score

    @property
    def round_number(self) -> int:
        return self._roundNumber

    @property
    def player_moves(self) -> MoveCollection:
        return self._playerMoves

    @property
    def opponent_moves(self) -> MoveCollection:
        return self._opponentMoves

    @property
    def player_score(self) -> int:
        return self._playerScore

    @property
    def opponent_score(self) -> int:
        return self._opponentScore
