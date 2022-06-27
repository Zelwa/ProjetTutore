from v4players.src.Move import Move
from v4players.src.Tile import Tile


class Grid:
    def __init__(self):
        size = 9
        self.grid = []
        for i in range(size):
            self.grid.append([])
            for j in range(size):
                self.grid[i].append("[]")
        self.grid[size // 2][size // 2] = Tile("Joker", 0)

        self.minX = size // 2
        self.maxX = size // 2
        self.minY = size // 2
        self.maxY = size // 2

    def deepCopy(self):
        newGrid = []
        for i in range(self.grid):
            newGrid.append([])
            for j in range(self.grid[0]):
                newGrid[i][j] = self.grid[i][j]
        copy = Grid()
        copy.setGrid(newGrid)
        return copy

    def setGrid(self, grid):
        self.grid = grid

    def getGrid(self):
        return self.grid

    def gridToString(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                print(self.grid[i][j], end=" ")
            print("")

    def calculScore(self):
        score = 0
        seen = {(len(self.grid) // 2, len(self.grid) // 2)}
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (i, j) not in seen and type(self.grid[i][j]) == Tile:
                    kingdom = [(i, j)]
                    kingdomCrowns = self.grid[i][j].getCrowns()
                    pos = 0
                    while pos < len(kingdom):
                        x, y = kingdom[pos]
                        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                            if 0 <= x2 < len(self.grid) and 0 <= y2 < len(self.grid[0]) and \
                                    (x2, y2) not in seen and type(self.grid[x2][y2]) == Tile and \
                                    self.grid[x2][y2].getLandscape() == self.grid[i][j].getLandscape():
                                kingdom.append((x2, y2))
                                kingdomCrowns += self.grid[x2][y2].getCrowns()
                                seen.add((x2, y2))
                        pos += 1
                    score += kingdomCrowns * len(kingdom)
        return score

    def getGridCrowns(self):
        gridcrowns = 0
        for k in range(len(self.grid)):
            for l in range(len(self.grid[0])):
                if type(self.grid[k][l]) == Tile:
                    gridcrowns += int(self.grid[k][l].getCrowns())
        return gridcrowns

    def validMoves(self, domino):
        valids = []
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if type(self.grid[i][j]) == str:  # premiere case vide a recevoir une tuile du domino
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and type(
                                self.grid[x][y]) == Tile:  # tuile "d'attache"
                            if self.grid[x][y].getLandscape() == domino.getTile1().getLandscape() or \
                                    self.grid[x][y].getLandscape() == "Joker":
                                for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                                    if 0 <= i2 < len(self.grid) and 0 <= j2 < len(self.grid[0]) and type(self.grid[i2][
                                                                                                             j2]) == str:  # seconde case vide a recevoir une tuile du domino
                                        valids.append(Move(i, j, i2, j2, domino))

                            if self.grid[x][y].getLandscape() == domino.getTile2().getLandscape() or \
                                    self.grid[x][y].getLandscape() == "Joker":
                                for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                                    if 0 <= i2 < len(self.grid) and 0 <= j2 < len(self.grid[0]) and type(self.grid[i2][
                                                                                                             j2]) == str:  # seconde case vide a recevoir une tuile du domino
                                        valids.append(Move(i2, j2, i, j, domino))
        return valids

    def add(self, move):
        tile1 = move.getDomino().getTile1()
        self.grid[move.getCoordTile1()[0]][move.getCoordTile1()[1]] = tile1

        tile2 = move.getDomino().getTile2()
        self.grid[move.getCoordTile2()[0]][move.getCoordTile2()[1]] = tile2

        for i in [move.getCoordTile1()[0], move.getCoordTile2()[0]]:
            if i < self.minX:
                self.minX = i
            elif i > self.maxX:
                self.maxX = i
        for j in [move.getCoordTile1()[1], move.getCoordTile2()[1]]:
            if j < self.minY:
                self.minY = j
            elif j > self.maxY:
                self.maxY = j

        self.narrowing()

    # Retrecissement de la grille
    def narrowing(self):
        deltaX = self.maxX - self.minX
        if deltaX < 4:
            fillableSpace = 4 - deltaX
            for nbLinesToDelete in range(self.minX - fillableSpace):
                self.grid.pop(0)
                self.minX -= 1
                self.maxX -= 1
            for nbLinesToDelete in range(((len(self.grid) - 1) - fillableSpace) - self.maxX):
                self.grid.pop(len(self.grid) - 1)

        else:
            if self.maxX == len(self.grid) - 1:
                for nbLinesToDelete in range(len(self.grid) - 5):
                    self.grid.pop(0)

            else:
                for nbLinesToDelete in range(len(self.grid) - 5):
                    self.grid.pop(len(self.grid) - 1)

        deltaY = self.maxY - self.minY
        if deltaY < 4:
            fillableSpace = 4 - deltaY
            for nbRowsToDelete in range(self.minY - fillableSpace):
                for nbLine in range(len(self.grid)):
                    self.grid[nbLine].pop(0)
                self.minY -= 1
                self.maxY -= 1
            for nbRowsToDelete in range(((len(self.grid[0]) - 1) - fillableSpace) - self.maxY):
                for nbLine in range(len(self.grid)):
                    self.grid[nbLine].pop(len(self.grid[nbLine]) - 1)

        else:
            if self.maxY == len(self.grid[0]) - 1:
                for nbRowsToDelete in range(len(self.grid[0]) - 5):
                    for nbLine in range(len(self.grid)):
                        self.grid[nbLine].pop(0)

            else:
                for nbRowsToDelete in range(len(self.grid[0]) - 5):
                    for nbLine in range(len(self.grid)):
                        self.grid[nbLine].pop(len(self.grid[nbLine]) - 1)
