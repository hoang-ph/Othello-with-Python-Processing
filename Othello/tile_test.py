from tile import Tile

BLACK = 0
WHITE = 255


def test__init__():
    """Test the constructor"""
    tile = Tile(50, 50, 100, BLACK)
    assert (tile.x == 50 and tile.y == 50 and tile.SIZE == 90
            and tile.color == BLACK)
    tile = Tile(100, 150, 100, WHITE)
    assert (tile.x == 100 and tile.y == 150 and tile.SIZE == 90
            and tile.color == WHITE)
