from board import Board
from game_controller import GameController

WHITE = 255
BLACK = 0


def test__init__():
    """A test for board constructor"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    assert(board.gc == gc
           and board.WIDTH == 600
           and board.HEIGHT == 600
           and board.SIZE == 8
           and board.WHITE == WHITE
           and board.BLACK == BLACK
           and board.BOX_SIZE == 600/8)
    i_mid = board.SIZE // 2
    j_mid = board.SIZE // 2
    for i in range(board.SIZE):
        for j in range(board.SIZE):
            if i == i_mid and j == j_mid:
                assert board.tiles[i][j].color == board.WHITE
            elif i == i_mid-1 and j == j_mid:
                assert board.tiles[i][j].color == board.BLACK
            elif i == i_mid-1 and j == j_mid-1:
                assert board.tiles[i][j].color == board.WHITE
            elif i == i_mid and j == j_mid-1:
                assert board.tiles[i][j].color == board.BLACK
            else:
                assert board.tiles[i][j] is None
    spacing = board.BOX_SIZE//2
    for i in range(board.SIZE):
        for j in range(board.SIZE):
            assert (board.tile_locations[i][j] ==
                   ((board.BOX_SIZE*j + spacing),
                   (board.BOX_SIZE*i + spacing)))


def test_place_tile():
    """A test for place_tile()"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    board.place_tile(0, 0, board.WHITE)
    assert board.tiles[0][0] is not None
    assert board.tiles[0][0].color == board.WHITE
    assert board.tiles[0][0].x == board.BOX_SIZE//2
    assert board.tiles[0][0].y == board.BOX_SIZE//2

    board.place_tile(0, 1, board.BLACK)
    assert board.tiles[0][1].color == board.BLACK
    assert board.tiles[0][1].x == board.BOX_SIZE//2 + board.BOX_SIZE
    assert board.tiles[0][1].y == board.BOX_SIZE//2

    board.place_tile(0, 0, board.BLACK)
    assert board.tiles[0][1].color == board.BLACK


def test_get_legal_moves():
    """A test for get_legal_moves()"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    legal_moves = board.get_legal_moves(board.WHITE)
    assert ((0, 2) in legal_moves
            and (1, 3) in legal_moves
            and (2, 0) in legal_moves
            and (3, 1) in legal_moves)

    legal_moves = board.get_legal_moves(board.BLACK)
    assert ((1, 0) in legal_moves
            and (0, 1) in legal_moves
            and (2, 3) in legal_moves
            and (3, 2) in legal_moves)


def test_check_legal_move():
    """A test for check_legal_move()"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    assert board.check_legal_move(0, 1, board.BLACK) is True
    assert board.check_legal_move(1, 0, board.BLACK) is True
    assert board.check_legal_move(2, 3, board.BLACK) is True
    assert board.check_legal_move(3, 2, board.BLACK) is True
    assert board.check_legal_move(2, 2, board.BLACK) is False
    assert board.check_legal_move(1, 2, board.BLACK) is False

    assert board.check_legal_move(0, 2, board.WHITE) is True
    assert board.check_legal_move(1, 3, board.WHITE) is True
    assert board.check_legal_move(3, 1, board.WHITE) is True
    assert board.check_legal_move(2, 0, board.WHITE) is True


def test_get_flip_tile_list():
    """A test for get_flip_tile_list"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    flip_list = board.get_flip_tile_list(1, 0, board.BLACK)
    assert (1, 1) in flip_list
    assert len(flip_list) == 1
    flip_list = board.get_flip_tile_list(1, 0, board.WHITE)
    assert len(flip_list) == 0
    flip_list = board.get_flip_tile_list(1, 3, board.WHITE)
    assert (1, 2) in flip_list
    assert len(flip_list) == 1


def test_check_legal_index():
    """A test for check_legal_index()"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    for i in range(board.SIZE):
        for j in range(board.SIZE):
            assert board.check_legal_index(i, j) is True
    assert board.check_legal_index(4, 4) is False


def test_flip_tiles():
    """A test for flip_tiles"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    assert board.tiles[1][1].color == board.WHITE
    board.flip_tiles(1, 0, board.BLACK)
    assert board.tiles[1][1].color == board.BLACK
    board.flip_tiles(0, 0, board.BLACK)
    assert board.tiles[0][0] is None


def test_update_scores():
    """A test for update_scores"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    board.update_scores()
    assert gc.player_score == 2 and gc.computer_score == 2
    board.place_tile(0, 0, board.BLACK)
    board.place_tile(0, 1, board.BLACK)
    board.place_tile(0, 2, board.BLACK)
    board.place_tile(0, 3, board.BLACK)
    board.update_scores()
    assert gc.player_score == 6 and gc.computer_score == 2
    board.place_tile(3, 0, board.WHITE)
    board.place_tile(3, 1, board.WHITE)
    board.place_tile(3, 2, board.WHITE)
    board.place_tile(3, 3, board.WHITE)
    board.update_scores()
    assert gc.player_score == 6 and gc.computer_score == 6


def test_board_filled():
    """A test for board_filled()"""
    gc = GameController()
    board = Board(600, 600, 4, gc, WHITE, BLACK)
    assert board.board_filled() is False
    for i in range(board.SIZE):
        for j in range(board.SIZE):
            board.place_tile(i, j, board.BLACK)
    assert board.board_filled() is True
