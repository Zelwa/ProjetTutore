from v4players.src.Grid import Grid
from v4players.src.Move import Move

class ExpectedMaxPlayer:
    def __init__(self, name):
        self.grid = Grid()
        self.name = name

    def validMoves(self, roundDraw):
        validMoves = []
        for i in range(len(roundDraw)):
            validMoves.extend(self.grid.validMoves(roundDraw[i]))
        return validMoves

    def chooseMove(self, roundDraw):
         scoreMax = 0
         bestMove= Move(-1, -1, -1, -1, roundDraw[0])
         validMoves = self.validMoves(roundDraw)
         for i in range(len(validMoves)): #Profondeur 1
             tmpGrid = self.grid.gridCopy()
             tmpGrid.add(validMoves[i])
             if(tmpGrid.calculScore()>scoreMax):
                 scoreMax = tmpGrid.calculScore()
                 bestMove = validMoves[i]
         return bestMove

    def chooseMoveDeep(self,roundDraw, draw): # Ne fonctionne pas
        bestMove = Move(-1, -1, -1, -1, roundDraw[0])
        bestMedium = 0
        validMoves = self.validMoves(roundDraw)
        for i in range(len(validMoves)):
            tmpGrid = self.grid.gridCopy()
            tmpGrid.add(validMoves[i])
            medium = []
            validMovesDraw = tmpGrid.validMoves(draw)
        for j in range(len(validMovesDraw)):
            tmpGrid2 = self.grid.gridCopy()
            tmpGrid2.add(validMoves[j])
            medium.append(tmpGrid2.calculScore())
        medium = sum(medium)/len(medium)
        if medium > bestMedium:
            bestMedium = medium
            bestMove = validMoves[i]
        return bestMove

    def playMove(self, move):
        self.grid.add(move)

    def getScore(self):
        return self.grid.calculScore()

    def getGrid(self):
        return self.grid

    def getCrowns(self):
        return self.grid.getGridCrowns()

    def __str__(self):
        return self.name
