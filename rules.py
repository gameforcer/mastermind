from collections import Counter
from random import sample, randint

class gameRules:
    
    def __init__(self):
        self._tries = 0
        self._total_turns = 12
        self.genKey()

    def setGuess(self, vals:list):
        self._guess = vals

    def genKey(self):
        self._key = sample(range(1, 6 + 1), 4)

    def chckCorrect(self):
        self._correct_pos = sum( i ==  j for i, j in zip(self._guess, self._key))
        self._correct_num = sum((Counter(self._guess) & Counter(self._key)).values())
        print(str(self._correct_pos) +" "+ str(self._correct_num) +" (klucz: "+str(self._key)+")")

    def getCrctPos(self):
        return self._correct_pos

    def getCrctNum(self):
        return self._correct_num

    def getTries(self):
        return self._tries


class normalMode(gameRules):
    def runTurn(self):
        self._tries += 1
        self.chckCorrect()
        if self._tries < self._total_turns:
            if self._guess == self._key:
                self._result_flag = True
        else:
            self._result_flag = False


class cheatMode(gameRules):
    def runTurn(self):
        self._tries += 1
        self.chckCorrect()
        if self._tries < self._total_turns:

            if randint(0, 2):
                self.chckCorrect()
            else:
                self._correct_pos = randint(1, 4)
                self._correct_num = randint(1, 4)

            if self._guess == self._key:
                self._result_flag = True
        else:
            self._result_flag = False

