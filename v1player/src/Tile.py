class Tile:
    def __init__(self, landscape, crowns):
        self.landscape = landscape
        self.crowns = crowns

    def getLandscape(self):
        return self.landscape

    def getCrowns(self):
        return self.crowns

    def __str__(self):
        ls = {"Champ": "C",
              "Foret": "F",
              "Ocean": "O",
              "Prairie": "P",
              "Desert": "D",
              "Mine": "M",
              "Joker": "X"
              }
        res = ls[self.landscape] + str(self.crowns)
        return res