from game.minimax import minimax, check_winner

def make_ai_move(board):
    """
    AI chooses the best move using minimax
    """
    best_move = None
    best_score = -float('inf')

    for i in range(9):
        if board.cells[i] == ' ':
            board.cells[i] = 'O'
            score = minimax(board.cells, False)
            board.cells[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board.cells[best_move] = 'O'


def is_game_over(board):
    """
    Check if the game has ended
    """
    return check_winner(board.cells)
