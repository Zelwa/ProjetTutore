import random

from v4players.src.Domino import Domino
from v4players.src.Tile import Tile


class Game:
    # Constructeur de la classe Game
    def __init__(self, players):
        self.drawingPlayerOrder = players
        self.gameDeck = []
        self.roundDraw = []

    # Initialisation de la pioche (draw) et de la petite pioche
    def initialization(self):
        tileC = Tile("Champ", 0)
        tileC1 = Tile("Champ", 1)
        tileO = Tile("Ocean", 0)
        tileO1 = Tile("Ocean", 1)
        tileF = Tile("Foret", 0)
        tileF1 = Tile("Foret", 1)
        tileP = Tile("Prairie", 0)
        tileP1 = Tile("Prairie", 1)
        tileP2 = Tile("Prairie", 2)
        tileD = Tile("Desert", 0)
        tileD1 = Tile("Desert", 1)
        tileD2 = Tile("Desert", 2)
        tileM = Tile("Mine", 0)
        tileM1 = Tile("Mine", 1)
        tileM2 = Tile("Mine", 2)
        tileM3 = Tile("Mine", 3)

        self.gameDeck = [Domino(tileC, tileC, 1), Domino(tileC, tileC, 2), Domino(tileF, tileF, 3), Domino(tileF, tileF, 4),
                         Domino(tileF, tileF, 5), Domino(tileF, tileF, 6), Domino(tileO, tileO, 7), Domino(tileO, tileO, 8),
                         Domino(tileO, tileO, 9), Domino(tileP, tileP, 10), Domino(tileP, tileP, 11), Domino(tileD, tileD, 12),
                         Domino(tileC, tileF, 13), Domino(tileO, tileC, 14), Domino(tileC, tileP, 15), Domino(tileC, tileD, 16),
                         Domino(tileF, tileO, 17), Domino(tileF, tileC, 18), Domino(tileC1, tileF, 19), Domino(tileC1, tileO, 20),
                         Domino(tileC1, tileP, 21), Domino(tileC1, tileD, 22), Domino(tileC1, tileM, 23), Domino(tileF1, tileC, 24),
                         Domino(tileF1, tileC, 25), Domino(tileF1, tileC, 26), Domino(tileF1, tileC, 27), Domino(tileF1, tileO, 28),
                         Domino(tileF1, tileP, 29), Domino(tileO1, tileC, 30), Domino(tileO1, tileP, 31), Domino(tileO1, tileF, 32),
                         Domino(tileO1, tileF, 33), Domino(tileO1, tileF, 34), Domino(tileO1, tileF, 35), Domino(tileP1, tileC, 36),
                         Domino(tileP1, tileO, 37), Domino(tileD1, tileC, 38), Domino(tileD1, tileP, 39), Domino(tileM1, tileC, 40),
                         Domino(tileP2, tileC, 41), Domino(tileP2, tileO, 42), Domino(tileD2, tileC, 43), Domino(tileD2, tileP, 44),
                         Domino(tileM2, tileC, 45), Domino(tileM2, tileD, 46), Domino(tileM2, tileD, 47), Domino(tileM3, tileC, 48)]

        self.fourDominosDraw()
        random.shuffle(self.drawingPlayerOrder)

    def playRound(self):
        nextDrawingOrder = []
        for currentPlayer in self.drawingPlayerOrder:
            move = currentPlayer.chooseMove(self.roundDraw)

            print(str(currentPlayer) + " pioche le domino " + str(move.getDomino()))
            currentPlayer.playMove(move)

            currentPlayer.getGrid().gridToString()

            dominoPicked = move.getDomino()
            self.roundDraw.remove(dominoPicked)
            nextDrawingOrder.append((currentPlayer, dominoPicked))

        nextDrawingOrder.sort(key=lambda tuple: tuple[1].getNumber())
        self.drawingPlayerOrder = [nextDrawingOrder[i][0] for i in range(len(nextDrawingOrder))]

        self.roundDraw.clear()
        if len(self.gameDeck) != 0:
            self.fourDominosDraw()

    def fourDominosDraw(self):
        if len(self.gameDeck) != 4:
            for i in range(4):
                randomDominoNumber = random.randint(0, (len(self.gameDeck)-1) - i)
                self.roundDraw.append(self.gameDeck.pop(randomDominoNumber))
        else:
            self.roundDraw = self.gameDeck

    def getWinner(self):
        winner = 0
        tmp = 0
        for player in self.drawingPlayerOrder:
            if player.getScore() > tmp:
                tmp = player.getScore()
                winner = player
        return winner

    def getDeck(self):
        return self.gameDeck

    def getDraw(self):
        return self.roundDraw

    def setDeck(self, deck):
        self.gameDeck = deck

    def setDraw(self, draw):
        self.roundDraw = draw

    def deepCopy(self):
        copyDrawingPlayerOrder = [player.deepCopy() for player in self.drawingPlayerOrder]
        copy = Game(copyDrawingPlayerOrder)
        copy.setDeck(self.gameDeck)
        copy.setDraw(self.roundDraw)
        return copy
