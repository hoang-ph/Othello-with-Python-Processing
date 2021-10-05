class Player:
    """A class for player to interact with the Othello game"""
    def __init__(self, board, game_controller, tile_color):
        self.board = board
        self.gc = game_controller
        self.tile_color = tile_color

    def place_tile(self, mouseX, mouseY):
        """
        :type mouseX: Float
        :type mouseY: Float
        :rtype: void
        Get mouse input location and place a tile on the board if
        it is a valid move
        """
        self.legal_moves = self.board.get_legal_moves(self.tile_color)
        if len(self.legal_moves) == 0:
            self.gc.player_no_move = True
            self.gc.swap_turn()
            print("No move available, computer's turn")

        i = mouseY // self.board.BOX_SIZE
        j = mouseX // self.board.BOX_SIZE
        if (i, j) in self.legal_moves:
            self.board.place_tile(i, j, self.tile_color)
            self.board.flip_tiles(i, j, self.tile_color)
            self.gc.swap_turn()
            print("Computer's turn")
