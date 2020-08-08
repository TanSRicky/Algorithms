from Player.Player import RandomComputerPlayer
from Player.Player import HumanPlayer

from Board.Board import TerminalBoard
from pathlib import Path

import sys
sys.setrecursionlimit(150000)
board_data = [0,0,0,0,0,0,0,0,0]
#board_data = ['X','O','X','X','O',0,0,0,'O']
board = TerminalBoard(board_data) 
board.play()




