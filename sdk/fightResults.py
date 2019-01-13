from sdk.fightResultType import FightResultType
from sdk.fightResultErrorType import FightResultErrorType


class FightResults:
    def __init__(self,
                 player_score: int,
                 opponent_score: int,
                 result: FightResultType,
                 is_error=False,
                 error_message: str = None,
                 error_type: FightResultErrorType = None,
                 round_results=None):
        self._playerScore = player_score
        self._opponentScore = opponent_score
        self._result = result
        self._isError = is_error
        self._errorMessage = error_message
        self._errorType = error_type
        self._roundResults = round_results

    @staticmethod
    def draw(player_score, opponent_score):
        return FightResults(player_score, opponent_score, FightResultType.Draw)

    @staticmethod
    def win(player_score, opponent_score):
        return FightResults(player_score, opponent_score, FightResultType.Win)

    @staticmethod
    def lost(player_score, opponent_score):
        return FightResults(player_score, opponent_score, FightResultType.Lost)

    @staticmethod
    def error(error_type, result, error_message):
        return FightResults(0, 0, result, True, error_message, error_type)

    def set_round_results(self, results):
        self._roundResults = results
        return self

    @property
    def player_score(self) -> int:
        return self._playerScore

    @property
    def opponent_score(self) -> int:
        return self._opponentScore

    @property
    def result(self) -> FightResultType:
        return self._result

    @property
    def is_error(self) -> bool:
        return self._isError

    @property
    def error_message(self) -> str:
        return self._errorMessage

    @property
    def error_type(self) -> FightResultErrorType:
        return self._errorType

    @property
    def round_results(self):
        return self._roundResults

    def __str__(self):
        if self.is_error:
            return "%s with error : %s - message: %s" % (self._result, self._errorType, self._errorMessage)
        return "%s: PlayerScore: %s, OpponentScore: %s" % (self._result, self._playerScore, self._opponentScore)
