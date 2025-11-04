import sys
import os

# Add absolute gui folder to Python path
sys.path.append(os.path.join(r"C:\Users\Varshika\Desktop\rep\CODSOFT\TASK2_TIC_TAC_TOE", "gui"))

import tkinter as tk
from tic_tac_toe_gui import TicTacToeGUI  
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Tic-Tac-Toe vs AI")
    window.geometry("400x400")  
    game_app = TicTacToeGUI(window)

    window.mainloop()
