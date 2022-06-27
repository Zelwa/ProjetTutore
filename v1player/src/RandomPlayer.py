import random

from v1player.src.Grid import Grid
from v1player.src.Move import Move


class RandomPlayer:
    def __init__(self, name):
        self.grid = Grid()
        self.name = name

    def validMoves(self, roundDraw):
        validMoves = []
        for i in range(len(roundDraw)):
            validMoves.extend(self.grid.validMoves(roundDraw[i]))
        return validMoves

    def chooseMove(self, gameState):
        validMoves = self.validMoves(gameState.getDraw())
        if len(validMoves) == 0:
            move = Move(-1, -1, -1, -1, random.choice(gameState.getDraw()))
        else:
            move = random.choice(validMoves)
        return move

    def playMove(self, move, displaying=False):
        if move.getCoordTile1() != (-1, -1):
            self.grid.add(move)
        elif displaying:
            print("Défausse du domino, pas de coup jouable")

    def getScore(self):
        return self.grid.calculScore()

    def getGrid(self):
        return self.grid

    def setGrid(self, grid):
        self.grid = grid

    def getCrowns(self):
        return self.grid.getGridCrowns()

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def deepCopy(self):
        copy = RandomPlayer(self.name)
        copy.setGrid(self.grid.deepCopy())
        return copy

    def reset(self):
        return RandomPlayer(self.name)
