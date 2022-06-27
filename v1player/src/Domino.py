class Domino:
    def __init__(self, tile1, tile2, number):
        self.tile1 = tile1
        self.tile2 = tile2
        self.number = number

    def getTile1(self):
        return self.tile1

    def getTile2(self):
        return self.tile2

    def getNumber(self):
        return self.number

    def __str__(self):
        res = str(self.tile1) + "|" + str(self.tile2) + "(" + str(self.number) + ")"
        return res
