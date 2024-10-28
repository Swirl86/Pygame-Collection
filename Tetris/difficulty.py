from enum import Enum

class Option:
    name: str
    point_inc: int

class Difficulty(Option, Enum):
    NONE = ("None", 1)
    EASY = ("Easy", 1)
    MEDIUM = ("Medium", 2)
    HARD = ("Hard", 4)

    @property
    def name(self):
        return self.value[0]

    @property
    def point_increment(self):
        return self.value[1]

    @staticmethod
    def get_names():
        return [difficulty.name for difficulty in Difficulty]

    @staticmethod
    def get_by_value(difficulty_str):
        for difficulty in Difficulty:
            if difficulty.name == difficulty_str:
                return difficulty
        raise ValueError("Invalid difficulty level")