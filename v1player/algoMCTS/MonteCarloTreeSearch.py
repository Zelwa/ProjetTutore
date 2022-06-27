import random

from v1player.src.Move import Move
from v1player.algoMCTS.Node import Node
from v1player.algoMCTS.Tree import Tree
from v1player.algoMCTS.UCT import UCT


class MonteCarloTreeSearch:
    def __init__(self, iterations):
        self.nbIterations = iterations

    def findNextMove(self, state):
        rootNode = Node(state)
        if len(state.getDeck()) == 0:
            rootNode.setTerminal()
        MCT = Tree(rootNode)

        for i in range(self.nbIterations):
            selectedNode = self.selection(MCT)
            if selectedNode.isTerminal():
                simulationStartingNode = selectedNode
            else:
                simulationStartingNode = self.expansion(MCT, selectedNode)
            won = self.simulation(simulationStartingNode)
            self.backPropagation(MCT, simulationStartingNode, won)

        bestNode = (MCT.getChilds(MCT.getRoot())[0], MCT.getChilds(MCT.getRoot())[0].getNbWins())
        for node in MCT.getChilds(MCT.getRoot())[1:]:
            if node.getNbWins() > bestNode[1]:
                bestNode = (node, node.getNbWins())
        return MCT.getAction(bestNode[0])

    def selection(self, tree):
        nextNode = tree.getRoot()
        while nextNode.isExpanded():
            if nextNode.isTerminal():
                return nextNode
            nextNode = UCT.findBestNodeUCT(nextNode, tree.getChilds(nextNode))
        nextNode.setExpanded()
        return nextNode

    def expansion(self, tree, node):
        validMoves = node.getState().getPlayer().validMoves(node.getState().getDraw())
        if len(validMoves) == 0:
            validMoves.append(Move(-1, -1, -1, -1, random.choice(node.getState().getDraw())))

        listNewNodes = []

        for move in validMoves:
            newNode = Node()
            newState = node.getState().deepCopy()

            newState.playMove(move)
            if len(newState.getDeck()) == 0:
                newNode.setTerminal()

            newNode.setState(newState)
            listNewNodes.append(newNode)
            tree.addFather(newNode, node)
            tree.addAction(newNode, move)

        return random.choice(listNewNodes)

    def simulation(self, node):
        finalScore = node.getState().playRandomGame()
        if finalScore > 40:
            return True
        return False

    def backPropagation(self, tree, node, won):
        while node is not None:
            node.incrementVisits()
            if won:
                node.incrementWins()
            node = tree.getFather(node)






