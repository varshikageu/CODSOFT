import tkinter as tk
from gui.tic_tac_toe_gui import TicTacToeGUI
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Tic-Tac-Toe vs AI")
    window.geometry("400x400")  
    game_app = TicTacToeGUI(window)

    window.mainloop()
