class Move:

    def __init__(self, x1, y1, x2, y2, domino):
        self.coordTile1 = (x1, y1)
        self.coordTile2 = (x2, y2)
        self.domino = domino

    def getCoordTile1(self):
        return self.coordTile1

    def getCoordTile2(self):
        return self.coordTile2

    def getDomino(self):
        return self.domino

    def __str__(self):
        return "(" + str(self.domino.getTile1()) + ":" + str(self.coordTile1[0]) + "," + str(self.coordTile1[1]) + \
               ")(" + str(self.domino.getTile2()) + ":" + str(self.coordTile2[0]) + "," + str(self.coordTile2[1]) + ")"
