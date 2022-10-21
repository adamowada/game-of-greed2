# from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(dice):
        dice = {i: dice.count(i) for i in dice}
        if len(dice) > 6:
            raise Exception('boo you cheat')
        if len(dice) == 6 or all([i == 2 for i in list(dice.values())]):
            return 1500
        if all([i == 3 for i in list(dice.values())]):
            return sum([(i * 100 if i > 1 else i * 1000) for i in dice])
        score = sum([(100 * dice[v] if i else 50 * dice[v]) if dice[v] <= 2 else (1000 * (dice[v] - 2) if i else 500 * (dice[v] - 2)) for i, v in enumerate([5, 1]) if v in dice])
        return score + sum([((dice[i] - 2) * 100 * i if dice[i] >= 3 else 0) for i in dice if i != 1 and i != 5])
