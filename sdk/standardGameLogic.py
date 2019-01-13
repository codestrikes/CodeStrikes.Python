class StandardGameLogic:
    @property
    def life_points(self) -> int:
        return 200

    @property
    def energy(self) -> int:
        return 12

    @property
    def max_rounds(self) -> int:
        return 100

    @property
    def max_move_time(self) -> int:
        return 500

    def calculate_score(self, attacker, defender) -> int:
        points = 0
        for attack in attacker.attacks:
            if not defender.has_defence(attack.area):
                points += attack.attack_power
        return points

    def validate(self, move_collection) -> bool:
        return move_collection.sum_energy() <= self.energy

    def validate_round(self, round_number, f1_points, f2_points) -> bool:
        if round_number >= self.max_rounds and f1_points > 0 and f2_points > 0:
            return False
        return f1_points >= 0 or f2_points >= 0
