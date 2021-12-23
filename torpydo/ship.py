from enum import Enum

class Color(Enum):
    CADET_BLUE = 1
    CHARTREUSE = 2
    ORANGE = 3
    RED = 4
    YELLOW = 5

class Letter(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8

class Position(object):
    def __init__(self, column: Letter, row: int, hit: bool = False):
        self.column = column
        self.row = row
        self.hit = hit

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return f"{self.column.name}{self.row}{self.hit}"

    __repr__ = __str__

class Ship(object):
    def __init__(self, name: str, size: int, color: Color, alive: bool = True):
        self.name = name
        self.size = size
        self.color = color
        self.alive = alive
        self.positions = []

    def add_position(self, input: str):
        letter = Letter[input.upper()[:1]]
        number = int(input[1:])
        position = Position(letter, number)

        self.positions.append(position)
    
    def check_is_alive(self):
        hits = 0
        for position in self.positions:
            if position.hit:
                hits = hits + 1
        if hits == len(self.positions):
            return False
        return True

    def __str__(self):
        return f"{self.color.name} {self.name} ({self.size}): {self.positions}"

    __repr__ = __str__
