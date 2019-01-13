from sdk.fightResultErrorType import FightResultErrorType
from sdk.fightResultType import FightResultType
from sdk.roundContext import RoundContext
from sdk.roundResult import RoundResult
from sdk.fightResults import FightResults


class Fight:
    def __init__(self, bot1, bot2, game_logic):
        self._bot1 = bot1
        self._bot2 = bot2
        self._gameLogic = game_logic

    def execute(self) -> FightResults:
        f1_move = None
        f2_move = None

        score1 = 0
        score2 = 0
        round: int = 0

        f1_lifepoints = self._gameLogic.life_points
        f2_lifepoints = self._gameLogic.life_points

        round_results = list()

        while f1_lifepoints > 0 and f2_lifepoints > 0:
            round += 1
            bot1_context = RoundContext(f2_move, score1, score2, f1_lifepoints, f2_lifepoints)

            try:
                moves = self._bot1.next_move(bot1_context)
                bot1_context.set_moves(moves)
            except Exception as exc:
                return FightResults.error(
                    FightResultErrorType.Runtime,
                    FightResultType.Lost,
                    str(exc)).set_round_results(round_results).set_round_results(round_results)

            if not self._gameLogic.validate(moves):
                return FightResults.error(
                    FightResultErrorType.IllegalMove,
                    FightResultType.Lost,
                    str(self._bot1) + " made an illegal move").set_round_results(round_results)

            bot2_context = RoundContext(f1_move, score2, score1, f2_lifepoints, f1_lifepoints)
            try:
                moves = self._bot2.next_move(bot2_context)
                bot2_context.set_moves(moves)
            except Exception as exc:
                return FightResults.error(FightResultErrorType.Runtime, FightResultType.Win, str(exc)).set_round_results(round_results)

            if not self._gameLogic.validate(moves):
                return FightResults.error(
                    FightResultErrorType.IllegalMove,
                    FightResultType.Win,
                    str(self._bot2) + " made an illegal move").set_round_results(round_results)

            f1_move = bot1_context.my_moves
            f2_move = bot2_context.my_moves

            score1 = self._gameLogic.calculate_score(f1_move, f2_move)
            score2 = self._gameLogic.calculate_score(f2_move, f1_move)

            f1_lifepoints -= score2
            f2_lifepoints -= score1

            round_result = RoundResult(round, f1_move, f2_move, score1, score2)
            round_results.append(round_result)

            if not self._gameLogic.validate_round(round, f1_lifepoints, f2_lifepoints):
                return FightResults.draw(f1_lifepoints, f2_lifepoints).set_round_results(round_results)

        if f1_lifepoints <= 0 and f2_lifepoints <= 0:
            return FightResults.draw(f1_lifepoints, f2_lifepoints).set_round_results(round_results)
        elif f1_lifepoints > f2_lifepoints:
            return FightResults.win(f1_lifepoints, f2_lifepoints).set_round_results(round_results)
        elif f1_lifepoints == f2_lifepoints:
            return FightResults.draw(f1_lifepoints, f2_lifepoints).set_round_results(round_results)

        return FightResults.lost(f1_lifepoints, f2_lifepoints).set_round_results(round_results)
