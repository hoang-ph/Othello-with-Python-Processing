from computer import Computer
from board import Board
from game_controller import GameController

BLACK = 0
WHITE = 255


def test__init__():
    """A test for computer constructor"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    computer = Computer(board, gc, WHITE)
    assert (computer.board == board and computer.gc == gc
           and computer.tile_color == WHITE
           and computer.legal_moves == [])

    computer = Computer(board, gc, BLACK)
    assert (computer.board == board and computer.gc == gc
           and computer.tile_color == BLACK
           and computer.legal_moves == [])


def test_get_corner_move():
    """A test for get_corner_move()"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    computer = Computer(board, gc, WHITE)
    index = computer.get_corner_move()
    assert index not in computer.legal_moves
    assert index is None

    computer.legal_moves = [(0, 0)]
    index = computer.get_corner_move()
    assert index == (0, 0)


def test_get_edge_move():
    """A test for get_corner_move()"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    computer = Computer(board, gc, WHITE)
    index = computer.get_edge_move()
    assert index not in computer.legal_moves
    assert index is None

    computer.legal_moves = [(0, 1), (7, 0)]
    index = computer.get_edge_move()
    assert index in computer.legal_moves
    assert index == (7, 0)


def test_get_best_move():
    """A test for get_best_move()"""
    gc = GameController()
    board = Board(600, 600, 8, gc, WHITE, BLACK)
    computer = Computer(board, gc, WHITE)
    index = computer.get_best_move()
    assert len(computer.legal_moves) == 0
    computer.legal_moves = board.get_legal_moves(computer.tile_color)
    assert len(computer.legal_moves) == 4
    assert (2, 4) in computer.legal_moves
    assert (3, 5) in computer.legal_moves
    assert (4, 2) in computer.legal_moves
    assert (5, 3) in computer.legal_moves
    index = computer.get_best_move()
    assert index in computer.legal_moves
    assert index == (2, 4)
