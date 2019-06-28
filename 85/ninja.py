scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = 'white yellow orange green blue brown black paneled red'.split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:

    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        for i in range(len(scores)-1):
            if new_score >= scores[i] and new_score < scores[i+1]:
                return BELTS[scores[i]]
        return None

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if type(new_score) != int:
            raise ValueError
        if new_score < self._score:
            raise ValueError
        if self._get_belt(new_score) != self._last_earned_belt:
            self._last_earned_belt = self._get_belt(new_score)
            print(f'Congrats, you earned {new_score} points obtaining the PyBites Ninja {self._last_earned_belt.capitalize()} Belt')
        else:
            print(f'Set new score to {new_score}')
        self._score = new_score
        
    score = property(_get_score, _set_score)