class GameController:
    """A class for managing the state of the game"""
    def __init__(self):
        """Create an instant of the game controller class"""
        self.player_turn = True
        self.computer_turn = False
        self.player_no_move = False
        self.computer_no_move = False
        self.player_score = 0
        self.computer_score = 0
        self.winner = None
        self.winner_score = 0
        self.loser_score = 0
        self.score_added = False
        self.player_name = None
        self.file_name = "scores.txt"

    def swap_turn(self):
        """
        :rtype: void
        Swap player_turn and computer_turn
        """
        if self.player_turn is True:
            self.player_turn = False
            self.computer_turn = True
        elif self.player_turn is False:
            self.player_turn = True
            self.computer_turn = False

    def no_move_available(self):
        """
        :rtype: Boolean
        Return True if no more available moves from player and
        computer, otherwise, return False
        """
        return self.player_no_move and self.computer_no_move

    def update_winner(self):
        """
        :rtype: void
        Set player_turn and computer_turn to None when the game ends
        and update winner score and loser score
        """
        self.player_turn = None
        self.computer_turn = None
        if self.player_score > self.computer_score:
            self.winner = self.player_name
            self.winner_score = self.player_score
            self.loser_score = self.computer_score
        elif self.player_score < self.computer_score:
            self.winner = "Computer"
            self.winner_score = self.computer_score
            self.loser_score = self.player_score
        else:
            self.winner = "Tie"
            self.winner_score = self.computer_score
            self.loser_score = self.winner_score

    def add_score(self):
        """
        :rtype: void
        Create scores.txt file and add the new score onto the top if it
        is the highest score, otherwise, add the score to the bottom of the
        file
        """
        print("Game ended!")
        print(self.winner + " wins. " + "Score: " + str(self.winner_score)
              + "-" + str(self.loser_score))

        new_score = self.player_name + " " + str(self.player_score)
        try:
            score_list = []
            f = open(self.file_name, "r+")
            for line in f:
                score_list.append(line.strip())

            top_score = int(score_list[0].split(" ")[-1])
            if self.player_score > top_score:
                f.seek(0, 0)
                previous_scores = "\n".join(score_list)
                f.write(new_score + "\n" + previous_scores)
            else:
                f.write("\n" + new_score)
            f.close()
            print("Your score is successfully added to " + self.file_name)
        except IOError:
            f = open(self.file_name, "w+")
            f.write(new_score)
            f.close()
            print(self.file_name + " is created and your score is"
                                 + " sucessfulled added.")

    def display(self, WIDTH, HEIGHT):
        """
        :type WIDTH: int
        :type HEIGHT: int
        :rtype: void
        Display the winner when the game ends
        """
        textSize(30)
        if self.winner == self.player_name:
            message = (self.winner + " wins! " + str(self.winner_score)
                       + "-" + str(self.loser_score))
        elif self.winner == "Computer":
            message = (self.player_name + " loses. " + str(self.loser_score)
                       + "-" + str(self.winner_score))
        else:
            message = ("Tie, " + str(self.winner_score) + "-"
                       + str(self.loser_score))

        stroke(2)
        fill(255)
        rectMode(CENTER)
        rect(WIDTH/2, HEIGHT/2, textWidth(message) + 20,
             textDescent() + textAscent() + 20)

        fill(204, 102, 0)
        textAlign(CENTER, CENTER)
        text(message, WIDTH//2, HEIGHT//2)
