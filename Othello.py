from enum import Enum;

class Direction(Enum):
    Left = 0; Right = 1; Up = 3; Down = 4

class Color(Enum):
    Black = 0; White =1

# Singleton class
class Game(object):
    __instance = None
    def __new__(cls, *args, **kwargs):
        if __instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized: return
        self.__initialized = True
        self.rows = 10
        self.cols = 10
        self.board = Board(self.rows, self.cols)
        self.players = (Player(Color.Black), Player(Color.White))

    def getBoard(self):
        return self.board

class Board:
    def __init__(self, rows, cols):
        self.blackCount = 0
        self.whiteCount = 0
        self.board = [[None for i in range(cols)] for j in range(rows)]

    def initialize(self):pass
    def placeColor(self, row, col, color):pass
    def flipSection(self, row, col, direction):pass
    def getScoreForColor(self, color):pass
    def updateScore(self, newColor, newPieces):pass

class Piece:
    def __init__(self, color):
        self.color = color
    def flip(self):
        if self.color == Color.Black: self.color = Color.White
        else: self.color = Color.Black
    def getColor(self): return self.color

class Player:
    def __init__(self, color):
        self.color = color
    def getScore(self):pass
    def playPiece(self, row, col):
        Game().getBoard().placeColor(row, col, self.color)
    def getColor(self): return self.color

if __name__ == "__main__":
    
