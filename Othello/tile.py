BORDER_GAP = 10


class Tile:
    """A class for a tile in Othello"""
    def __init__(self, x, y, BOX_SIZE, color):
        """Creates an instant of a tile given the color at (x,y) position"""
        self.x = x
        self.y = y
        self.color = color
        self.SIZE = BOX_SIZE - BORDER_GAP

    def display(self):
        """
        :rtype: void
        Draws the tile
        """
        fill(self.color)
        ellipse(self.x, self.y, self.SIZE, self.SIZE)
