import random

from v4players.src.Grid import Grid
from v4players.src.Move import Move


class RandomPlayer:
    def __init__(self, name):
        self.grid = Grid()
        self.name = name

    def validMoves(self, roundDraw):
        validMoves = []
        for i in range(len(roundDraw)):
            validMoves.extend(self.grid.validMoves(roundDraw[i]))
        return validMoves

    def chooseMove(self, roundDraw):
        validMoves = self.validMoves(roundDraw)
        if len(validMoves) == 0:  # Pas de coup jouable, pioche du domino le moins cher
            lessExpensiveDomino = 0
            tmp = 49
            for domino in roundDraw:
                if domino.getNumber() < tmp:
                    lessExpensiveDomino = domino
                    tmp = domino.getNumber()
            move = Move(-1, -1, -1, -1, lessExpensiveDomino)
        else:
            move = random.choice(validMoves)
        return move

    def playMove(self, move):
        if move.getCoordTile1() == (-1, -1):
            print("Défausse du domino, pas de coup jouable")
        else:
            self.grid.add(move)

    def getScore(self):
        return self.grid.calculScore()

    def getGrid(self):
        return self.grid

    def setGrid(self, grid):
        self.grid = grid

    def getCrowns(self):
        return self.grid.getGridCrowns()

    def __str__(self):
        return self.name

    def deepCopy(self):
        copy = RandomPlayer(self.name)
        copy.setGrid(self.grid.deepCopy())
        return copy
