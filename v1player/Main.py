from v1player.src.Game import Game
from v1player.src.MCPlayer import MCPlayer


def main():
    game = Game(MCPlayer("Joueur 1", 25))
    game.playGames(100)


if __name__ == "__main__":
    main()