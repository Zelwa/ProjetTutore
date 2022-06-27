class Tree:
    def __init__(self,  root):
        self.rootNode = root
        self.actions = {}
        self.fathers = {self.rootNode: None}

    def getRoot(self):
        return self.rootNode

    def getAction(self, node):
        return self.actions[node]

    def getFather(self, node):
        return self.fathers[node]

    def addAction(self, node, move):
        self.actions[node] = move

    def addFather(self, node, father):
        self.fathers[node] = father

    def getChilds(self, father):
        res = []
        for node, value in self.fathers.items():
            if value == father:
                res.append(node)
        return res
