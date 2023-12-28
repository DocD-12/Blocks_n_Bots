import game
import player


if __name__ == '__main__':
    mGame = game.Game(20)
    # mGame.set_time(90)
    mPlayer = player.Player(10, 12, mGame.tile_size)
    mPlayer.set_id(10)
    tRed = player.Team(0)
    tRed.add_player(mPlayer)
    mGame.add_team(tRed)

    mPlayer = player.Player(15, 2, mGame.tile_size)
    mPlayer.set_id(20)
    tBlue = player.Team(1)
    tBlue.add_player(mPlayer)
    mGame.add_team(tBlue)

    mGame.print_grid()
    mGame.start()
