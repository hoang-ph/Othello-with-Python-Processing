from game_controller import GameController


def test__init__():
    """Test game_controller constructor"""
    gc = GameController()
    assert(gc.player_turn is True
           and gc.computer_turn is False
           and gc.player_no_move is False
           and gc.computer_no_move is False
           and gc.player_score == 0
           and gc.computer_score == 0
           and gc.winner is None
           and gc.winner_score == 0
           and gc.loser_score == 0
           and gc.score_added is False
           and gc.player_name is None
           and gc.file_name == "scores.txt")


def test_swap_turn():
    """Test swap_turn()"""
    gc = GameController()
    gc.swap_turn()
    assert(gc.player_turn is False and gc.computer_turn is True)
    gc.swap_turn()
    assert(gc.player_turn is True and gc.computer_turn is False)
    gc.player_turn = None
    gc.swap_turn()
    assert(gc.player_turn is None and gc.computer_turn is False)


def test_no_move_available():
    """A test for no_move_available()"""
    gc = GameController()
    assert gc.no_move_available() is False
    gc.player_no_move = True
    gc.computer_no_move = True
    assert gc.no_move_available() is True


def test_update_winner():
    """A test for update_winner()"""
    gc = GameController()
    gc.player_score = 10
    gc.computer_score = 5
    gc.update_winner()
    assert (gc.winner == gc.player_name
            and gc.winner_score == 10
            and gc.loser_score == 5
            and gc.player_turn is None
            and gc.computer_turn is None)

    gc.player_score = 5
    gc.computer_score = 5
    gc.update_winner()
    assert (gc.winner == "Tie"
            and gc.winner_score == 5
            and gc.loser_score == 5
            and gc.player_turn is None
            and gc.computer_turn is None)

    gc.player_score = 5
    gc.computer_score = 10
    gc.update_winner()
    assert (gc.winner == "Computer"
            and gc.winner_score == 10
            and gc.loser_score == 5
            and gc.player_turn is None
            and gc.computer_turn is None)


def test_add_score():
    """A test for add_score()"""
    gc = GameController()
    gc.winner = "User0"
    gc.winner_score = 0
    gc.loser_score = 0
    gc.player_name = "User1"
    gc.player_score = 10
    gc.add_score()
    gc.player_name = "User2"
    gc.player_score = 15
    gc.add_score()
    gc.player_name = "User3"
    gc.player_score = 8
    gc.add_score()

    f = open(gc.file_name, "r")
    lines = []
    for line in f:
        lines.append(line.strip())
    assert lines[0] == "User2 15"
    assert lines[1] == "User1 10"
    assert lines[2] == "User3 8"
