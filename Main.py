import tkinter as tk

class BowlingLogic:
    def __init__(self):
        self.score = 0
        self.frame = 1
        self.roll = 1
        self.pins = 10
        self.strike = False
        self.spare = False
        self.strikeBonus = 0
        self.spareBonus = 0
        self.frameScore = 0
        self.rollScore = 0
        self.frameScores = []
        self.rollScores = []

    def knocked_pins(self, pins):
        self.rollScore = pins
        self.rollScores.append(pins)

        if self.strike:
            self.strikeBonus += pins
            if self.roll == 2:
                self.strike = False
                self.score += self.strikeBonus
                self.strikeBonus = 0

        if self.spare:
            self.spareBonus += pins
            self.spare = False
            self.score += self.spareBonus
            self.spareBonus = 0

        self.frameScore += pins

        if self.roll == 1:
            if pins == 10:  # Strike
                self.strike = True
                self.frameScores.append(self.frameScore)
                self.score += self.frameScore
                self.frameScore = 0
                self.frame += 1
            else:
                self.roll = 2
        elif self.roll == 2:
            if self.frameScore == 10:  # Spare
                self.spare = True
            self.frameScores.append(self.frameScore)
            self.score += self.frameScore
            self.frameScore = 0
            self.frame += 1
            self.roll = 1

        if self.frame > 10:
            print("Game Over")
        else:
            self.pins = 10 - self.rollScore if self.roll == 2 else 10

    def get_score(self):
        return self.score

    def get_frameScore(self):
        return self.frameScores


# Example usage:
game = BowlingLogic()

for _ in range(12):
    game.knocked_pins(10)
print(game.get_score())  # 300
print(game.get_frameScore())
