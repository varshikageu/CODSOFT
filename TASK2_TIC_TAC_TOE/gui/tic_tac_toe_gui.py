# tic_tac_toe_gui.py
import tkinter as tk
from tkinter import messagebox
from game.board import Board
from game.player import make_ai_move, is_game_over

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe AI")
        self.board = Board()
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        """
        Create 3x3 buttons for the board
        """
        for i in range(9):
            btn = tk.Button(
                self.root,
                text=' ',
                font=('Arial', 24),
                width=5,
                height=2,
                command=lambda i=i: self.human_move(i)
            )
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)

    def human_move(self, index):
        """
        Handle human click
        """
        if self.board.cells[index] == ' ':
            self.board.cells[index] = 'X'
            self.buttons[index].config(text='X', state='disabled')
            if self.check_end_game():
                return
            # Let AI play after a small delay
            self.root.after(200, self.ai_turn)

    def ai_turn(self):
        """
        AI plays its move
        """
        make_ai_move(self.board)
        for i in range(9):
            self.buttons[i].config(text=self.board.cells[i])
            if self.board.cells[i] != ' ':
                self.buttons[i].config(state='disabled')
        self.check_end_game()

    def check_end_game(self):
        winner = is_game_over(self.board)
        if winner:
            if winner == 'Draw':
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"{winner} wins!")
            self.root.destroy()
            return True
        return False
