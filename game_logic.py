# from collections import Counter


class GameLogic:
    @staticmethod
    def calculate_score(dice):
        # turn tuple into dictionary (you can and should use Counter() for this)
        dice = {i: dice.count(i) for i in dice}
        # calculate score for straight or triple pairs
        if len(dice) == 6 or all([i == 2 for i in list(dice.values())]):
            return 1500
        # calculate score for 1s and 5s 
        score = sum([(100 * dice[v] if i else 50 * dice[v]) if dice[v] <= 2 else (1000 * (dice[v] - 2) if i else 500 * (dice[v] - 2)) for i, v in enumerate([5, 1]) if v in dice])
        # calculate score for 2s, 3, 4s, and 6s
        return score + sum([((dice[i] - 2) * 100 * i if dice[i] >= 3 else 0) for i in dice if i != 1 and i != 5])
