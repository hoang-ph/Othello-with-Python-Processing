class Computer:
    """A class represent AI's move for Othello game"""
    def __init__(self, board, game_controller, tile_color):
        self.gc = game_controller
        self.board = board
        self.tile_color = tile_color
        self.legal_moves = []

    def place_tile(self):
        """
        :rtype: void
        Choose a suitable move from the available-move list
        """
        self.legal_moves = self.board.get_legal_moves(self.tile_color)
        if len(self.legal_moves) == 0:
            self.gc.computer_no_move = True
            self.gc.swap_turn()
            print("No move available, your turn")

        if self.gc.computer_turn:
            if self.get_corner_move():
                index = self.get_corner_move()
            elif self.get_edge_move():
                index = self.get_edge_move()
            else:
                index = self.get_best_move()
            i, j = index
            if self.board.check_legal_move(i, j, self.tile_color):
                self.board.place_tile(i, j, self.tile_color)
                self.board.flip_tiles(i, j, self.tile_color)
                self.gc.swap_turn()
                print("Your turn")

    def get_corner_move(self):
        """
        :rtype: Tuple(int i, int j) or None
        Return an index for corner move from the available legal moves list
        return None if not found a corner move available
        """
        corner_indexes = [(0, 0), (0, self.board.SIZE-1),
                          (self.board.SIZE-1, 0),
                          (self.board.SIZE-1, self.board.SIZE-1)]
        for index in corner_indexes:
            if index in self.legal_moves:
                return index
        return None

    def get_edge_move(self):
        """
        :rtype: Tuple(int i, int j) or None
        Return a tuple of [i,j] index if an edge move exist,
        otheweise, return None
        """
        edge_move_list = []
        for i in range(self.board.SIZE):
            edge_move_list.append((i, 0))
            edge_move_list.append((i, self.board.SIZE-1))
            edge_move_list.append((0, i))
            edge_move_list.append((self.board.SIZE-1, i))
        for index in edge_move_list:
            if index in self.legal_moves:
                return index
        return None

    def get_best_move(self):
        """
        :rtype: Tuple(int i, int j)
        Return a tuple of [i,j] index for the move with
        the most flippable tiles
        """
        count = 0
        i_best = 0
        j_best = 0
        for i, j in self.legal_moves:
            if (count
               < len(self.board.get_flip_tile_list(i, j, self.tile_color))):
                i_best, j_best = i, j
                count = len(self.board.get_flip_tile_list(i, j,
                                                          self.tile_color))
        return (i_best, j_best)
