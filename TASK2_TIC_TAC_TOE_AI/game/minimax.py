# minimax.py

def minimax(cells, is_ai_turn):
    """
    Simple recursive minimax implementation for Tic-Tac-Toe AI.
    Returns a score from AI perspective:
    +1 if AI (O) wins, -1 if human (X) wins, 0 for draw.
    """
    winner = check_winner(cells)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif winner == 'Draw':
        return 0

    if is_ai_turn:
        best_score = -float('inf')
        for i in range(9):
            if cells[i] == ' ':
                cells[i] = 'O'
                score = minimax(cells, False)
                cells[i] = ' '
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if cells[i] == ' ':
                cells[i] = 'X'
                score = minimax(cells, True)
                cells[i] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def check_winner(cells):
    """
    Returns 'X' if human wins, 'O' if AI wins,
    'Draw' if board full and no winner, else None.
    """
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8), 
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6) 
    ]
    for a,b,c in win_positions:
        if cells[a] == cells[b] == cells[c] != ' ':
            return cells[a]
    if ' ' not in cells:
        return 'Draw'
    return None
