class Node:
    def __init__(self,  state=None):
        self.expanded = False
        self.terminal = False
        self.nbVisits = 0
        self.nbLeadsToWin = 0
        self.state = state

    def incrementVisits(self):
        self.nbVisits += 1

    def incrementWins(self):
        self.nbLeadsToWin += 1

    def getNbVisits(self):
        return self.nbVisits

    def getNbWins(self):
        return self.nbLeadsToWin

    def isTerminal(self):
        return self.terminal

    def setTerminal(self):
        self.terminal = True

    def isExpanded(self):
        return self.expanded

    def setExpanded(self):
        self.expanded = True

    def setState(self, game):
        self.state = game

    def getState(self):
        return self.state
