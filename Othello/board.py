from tile import Tile


class Board:
    """A class for the Othello board"""
    def __init__(self, WIDTH, HEIGHT, SIZE, game_controller, WHITE, BLACK):
        """Create an instant of a board with given width, height, and size"""
        self.gc = game_controller
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SIZE = SIZE
        self.WHITE = WHITE
        self.BLACK = BLACK
        self.BOX_SIZE = WIDTH / SIZE
        # Setup tiles nested list along with
        # the associated tile_location nested list
        self.tiles = [[None for _ in range(self.SIZE)]
                      for _ in range(self.SIZE)]
        self.tile_locations = [[((self.BOX_SIZE*j + self.BOX_SIZE//2),
                                 (self.BOX_SIZE*i + self.BOX_SIZE//2))
                                for j in range(self.SIZE)]
                               for i in range(self.SIZE)]
        self.setup()

    def setup(self):
        """
        :rtype: void
        Setup 4 starting tiles on the board
        """
        i_mid = self.SIZE // 2
        j_mid = self.SIZE // 2
        self.place_tile(i_mid, j_mid, self.WHITE)
        self.place_tile(i_mid-1, j_mid, self.BLACK)
        self.place_tile(i_mid-1, j_mid-1, self.WHITE)
        self.place_tile(i_mid, j_mid-1, self.BLACK)

    def place_tile(self, i, j, tile_color):
        """
        :type i: int
        :type j: int
        :type tile_color: int
        :rtype: void
        Create a tile at the given i,j index
        """
        i, j = int(i), int(j)
        x, y = self.tile_locations[i][j]
        self.tiles[i][j] = Tile(x, y, self.BOX_SIZE, tile_color)

    def get_legal_moves(self, tile_color):
        """
        :type tile_color: int
        :rtype: legal_moves: List[(int, int)]
        Return a list of indexes of legal moves
        """
        legal_moves = []
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if (self.tiles[i][j] is None
                   and self.check_legal_move(i, j, tile_color)):
                    legal_moves.append((i, j))
        return legal_moves

    def check_legal_move(self, i, j, tile_color):
        """
        :type i: int
        :type j: int
        :type tile_color: int
        :rtype: Boolean
        Return True if the given tile's [i,j] index is
        a legal move, otherwise, return False
        """
        if len(self.get_flip_tile_list(i, j, tile_color)) == 0:
            return False
        return True

    def get_flip_tile_list(self, i, j, tile_color):
        """
        :type i: int
        :type j: int
        :type tile_color: int
        :rtype: flip_tile_list: List[(int, int)]
        Return a list of flippable tiles given the starting
        [i,j] index and the color of the playing tile
        """
        flip_tile_list = []
        search_directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                             (1, -1),  (1, 0),  (1, 1)]
        # Search 8 directions from i,j indexes to find all flippable tiles
        for i_direction, j_direction in search_directions:
            temp_flip_list = []
            new_i = int(i + i_direction)
            new_j = int(j + j_direction)
            if self.check_legal_index(new_i, new_j):
                # Check if the next tiles are the opposite color
                tile = self.tiles[new_i][new_j]
                while tile is not None and tile.color != tile_color:
                    temp_flip_list.append((new_i, new_j))
                    new_i = new_i + i_direction
                    new_j = new_j + j_direction
                    if not self.check_legal_index(new_i, new_j):
                        break
                    tile = self.tiles[new_i][new_j]
                # Store all flippable tiles into the list
                if (tile is not None and tile.color == tile_color):
                    flip_tile_list.extend(temp_flip_list)
                else:
                    temp_flip_list = []
        return flip_tile_list

    def check_legal_index(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: Boolean
        Return True if the given [i,j] index is legal on the board
        """
        return (0 <= i < self.SIZE) and (0 <= j < self.SIZE)

    def flip_tiles(self, i, j, tile_color):
        """
        :type i: int
        :type j: int
        :type tile_color: int
        :rtype: void
        Change tiles' color of those inside
        the flip_tile_list
        """
        target_list = self.get_flip_tile_list(i, j, tile_color)
        for i, j in target_list:
            if self.tiles[i][j].color == self.BLACK:
                self.tiles[i][j].color = self.WHITE
            else:
                self.tiles[i][j].color = self.BLACK

    def update_scores(self):
        """
        :rtype: void
        Update the scores for player and computer
        """
        self.gc.player_score = 0
        self.gc.computer_score = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.tiles[i][j] is None:
                    continue
                elif self.tiles[i][j].color == self.BLACK:
                    self.gc.player_score += 1
                else:
                    self.gc.computer_score += 1

    def board_filled(self):
        """
        :rtype: Boolean
        Return True if the board is filled, otherwise, return False
        """
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.tiles[i][j] is None:
                    return False
        return True

    def display(self):
        """
        :rtype: void
        Display the Othello board game
        """
        # Display board's lines
        stroke(0)
        strokeWeight(2)
        for x in range(self.BOX_SIZE, self.HEIGHT, self.BOX_SIZE):
            line(x, 0, x, self.HEIGHT)
        for y in range(self.BOX_SIZE, self.WIDTH, self.BOX_SIZE):
            line(0, y, self.WIDTH, y)

        # Display tiles
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.tiles[i][j] is not None:
                    self.tiles[i][j].display()

        # Update scores
        self.update_scores()

        # Display when the game ends
        if self.board_filled() or self.gc.no_move_available():
            self.gc.update_winner()
            self.gc.display(self.WIDTH, self.HEIGHT)
            if not self.gc.score_added:
                self.gc.add_score()
                self.gc.score_added = True
