from player import Player
from board import Board
from game_controller import GameController

BLACK = 0
WHITE = 255


def test__init__():
    """A test for Player constructor"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    player = Player(board, gc, BLACK)
    assert (player.board == board and player.gc == gc
           and player.tile_color == BLACK)

    player = Player(board, gc, WHITE)
    assert (player.board == board and player.gc == gc
           and player.tile_color == WHITE)


def test_place_tile():
    """A test for place_tile()"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    player = Player(board, gc, BLACK)
    player.place_tile(200, 250)
    assert len(player.legal_moves) == 4
    assert (3, 2) in player.legal_moves
    assert board.tiles[3][2].color == BLACK
    assert board.tiles[3][3].color == BLACK

    player.place_tile(0, 0)
    assert (0, 0) not in player.legal_moves
