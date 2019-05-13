from collections import Counter
from random import sample, randint

class GameRules:
    
    def __init__(self):
        self._tries = 0
        self._total_turns = 12
        self.gen_key()

    def set_guess(self, vals:list):
        self._guess = vals

    def gen_key(self):
        self._key = sample(range(1, 6 + 1), 4)

    def check_correct(self):
        self._correct_pos = sum( i ==  j for i, j in zip(self._guess, self._key))
        self._correct_num = sum((Counter(self._guess) & Counter(self._key)).values())
        print(f"{self._correct_pos} {self._correct_num} (key: {self._key})")

    def get_correct_pos(self):
        return self._correct_pos

    def get_correct_num(self):
        return self._correct_num

    def get_tries(self):
        return self._tries


class NormalMode(GameRules):
    def run_turn(self):
        self._tries += 1
        self.check_correct()
        if self._tries < self._total_turns:
            if self._guess == self._key:
                self._result_flag = True
        else:
            self._result_flag = False


class CheatMode(GameRules):
    def run_turn(self):
        self._tries += 1
        self.check_correct()
        if self._tries < self._total_turns:

            if randint(0, 1):
                self._correct_pos = randint(1, 3)
                self._correct_num = randint(1, 3)

            if self._guess == self._key:
                self._result_flag = True
        else:
            self._result_flag = False
