from board import Board
from game_controller import GameController
from computer import Computer
from player import Player

BACKGROUND = (0, 110, 0)
BLACK = 0
WHITE = 255
WIDTH = 640
HEIGHT = 640
SIZE = 8
DELAY = 70
count = 0

gc = GameController()
board = Board(WIDTH, HEIGHT, SIZE, gc, WHITE, BLACK)
player = Player(board, gc, BLACK)
computer = Computer(board, gc, WHITE)


def setup():
    background(*BACKGROUND)
    size(WIDTH, HEIGHT)
    gc.player_name = input('enter your name')
    if gc.player_name:
        print('Hi ' + gc.player_name)
        print("Your turn")
    else:
        gc.player_name = "Anonymous"
        print("Hi\nYour turn")


def input(self, message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    global count
    board.display()
    if gc.computer_turn:
        if count == DELAY:
            computer.place_tile()
            count = 0
        else:
            count += 1


def mouseClicked():
    if gc.player_turn:
        player.place_tile(mouseX, mouseY)
