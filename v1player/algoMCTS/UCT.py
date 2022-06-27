import sys
import math


class UCT:
    @staticmethod
    def uctValue(visits, node_visits, node_wins):
        if node_visits == 0:
            return float("inf")
        return (node_wins / node_visits) + (1.41 * math.sqrt(math.log(visits)) / node_visits)

    @staticmethod
    def findBestNodeUCT(node, node_childs):
        return max(node_childs, key=lambda x: UCT.uctValue(node.getNbVisits(), x.getNbVisits(), x.getNbWins()))
