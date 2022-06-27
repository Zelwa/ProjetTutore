from v4players.src.Game import Game
from v4players.src.RandomPlayer import RandomPlayer


def main():
    listPlayers=[RandomPlayer("Joueur 1"), RandomPlayer("Joueur 2"), RandomPlayer("Joueur 3"), RandomPlayer("Joueur 4")]
    game = Game(listPlayers)

    print("Initialisation de la partie")
    game.initialization()

    for i in range(12):
        for domino in game.roundDraw:
            print(domino, end=", ")
        print()
        game.playRound()
    print("Gagnant : " + str(game.getWinner()) + ", score : " + str(game.getWinner().getScore()))


if __name__ == "__main__":
    main()