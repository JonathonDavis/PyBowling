import unittest


class Bowling:
    def __init__(self,name="Player"):
        self.name = name
        self.rolls = [0]
        self.current_roll = 0

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Invalid number of pins knocked down")

        if self.current_roll < 21:
            self.rolls[self.current_roll] = pins
            self.current_roll += 1

        self.complete_remaining_rolls() # complete the remaining rolls for the other methods calculations.

    def complete_remaining_rolls(self):
        while len(self.rolls) < 21:
            self.rolls.append(0)  # fill the remaining rolls with 0
        if len(self.rolls) > 21:
            self.rolls = self.rolls[:21]

    def get_score(self):
        score = 0
        frame_index = 0

        for frame in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return score

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _sum_of_balls_in_frame(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def _strike_bonus(self, frame_index):
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        return self.rolls[frame_index + 2]

    def get_frameScore(self, frame):
        if frame < 1 or frame > 10:
            return "Invalid frame number"

        score = 0
        roll_index = 0
        for current_frame in range(1, frame + 1):
            if self._is_strike(roll_index):
                score += 10 + self._strike_bonus(roll_index)
                roll_index += 1
            elif self._is_spare(roll_index):
                score += 10 + self._spare_bonus(roll_index)
                roll_index += 2
            else:
                score += self._sum_of_balls_in_frame(roll_index)
                roll_index += 2

        return score

    def print_score_table(self):
        frames = [f"Frame {i+1}" for i in range(10)]
        rolls = []
        scores = []

        frame_index = 0
        for frame in range(10):
            if self._is_strike(frame_index):
                rolls.append("X")
                scores.append(self.get_frameScore(frame + 1))
                frame_index += 1
            elif self._is_spare(frame_index):
                rolls.append(f"{self.rolls[frame_index]} /")
                scores.append(self.get_frameScore(frame + 1))
                frame_index += 2
            else:
                rolls.append(f"{self.rolls[frame_index]} {self.rolls[frame_index + 1]}")
                scores.append(self.get_frameScore(frame + 1))
                frame_index += 2

        total_score = self.get_score()

        print(f"{'':<10}" + "".join([f"{frame:<12}" for frame in frames]) + "Total")
        print(f"{'Rolls':<10}" + "".join([f"{roll:<12}" for roll in rolls]) + "")
        print(f"{'Scores':<10}" + "".join([f"{score:<12}" for score in scores]) + f"{total_score:<10}")


