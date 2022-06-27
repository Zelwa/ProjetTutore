import random

from v1player.src.Grid import Grid
from v1player.src.Move import Move
from v1player.algoMCTS.MonteCarloTreeSearch import MonteCarloTreeSearch


class MCPlayer:
    def __init__(self, name, iter):
        self.grid = Grid()
        self.name = name
        self.nbIter = iter

    def validMoves(self, roundDraw):
        validMoves = []
        for i in range(len(roundDraw)):
            validMoves.extend(self.grid.validMoves(roundDraw[i]))
        return validMoves

    def chooseMove(self, gameState):
        mcts = MonteCarloTreeSearch(self.nbIter)
        return mcts.findNextMove(gameState)

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
        copy = MCPlayer(self.name, self.nbIter)
        copy.setGrid(self.grid.deepCopy())
        return copy

    def reset(self):
        return MCPlayer(self.name, self.nbIter)
