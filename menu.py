# Menu class
import word_search
import chess
import sudoku
import minesweeper

class Menu:    
    def __init__(self):
        self.ws_game = word_search.WordSearch()
        self.chess_game = chess.Chess()
        self.sudoku_game = sudoku.Sudoku()
        self.ms_game = minesweeper.Minesweeper()

    def printClass(self):
        print("This is the menu class.")
        self.ws_game.printClass()
        self.chess_game.printClass()
        self.sudoku_game.printClass()
        self.ms_game.printClass()

game = Menu()
game.printClass()