import game
import player


if __name__ == '__main__':
    mGame = game.Game(20)
    mPlayer = player.Player(2, 2, mGame.tile_size)
    tRed = player.Team(0)
    tRed.add_player(mPlayer)
    mGame.add_team(tRed)
    mGame.start()
