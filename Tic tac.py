import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')
    print("\n")

def available_moves():
    return [i for i, spot in enumerate(board) if spot == ' ']

def winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]              
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

def is_full():
    return ' ' not in board

def minimax(state, depth, alpha, beta, is_maximizing):
    if winner(state, 'O'):
        return {'score': 1}
    elif winner(state, 'X'):
        return {'score': -1}
    elif is_full():
        return {'score': 0}

    if is_maximizing:
        best = {'score': -math.inf}
        for move in available_moves():
            state[move] = 'O'
            sim = minimax(state, depth + 1, alpha, beta, False)
            state[move] = ' '
            sim['move'] = move

            if sim['score'] > best['score']:
                best = sim

            alpha = max(alpha, sim['score'])
            if beta <= alpha:
                break
        return best
    else:
        best = {'score': math.inf}
        for move in available_moves():
            state[move] = 'X'
            sim = minimax(state, depth + 1, alpha, beta, True)
            state[move] = ' '
            sim['move'] = move

            if sim['score'] < best['score']:
                best = sim

            beta = min(beta, sim['score'])
            if beta <= alpha:
                break
        return best

def ai_move():
    move = minimax(board, 0, -math.inf, math.inf, True)['move']
    board[move] = 'O'

def play():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board()

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a valid move (1-9).")
            continue

        board[move] = 'X'
        print_board()

        if winner(board, 'X'):
            print("You win!")
            break
        if is_full():
            print("It's a tie!")
            break

        print("AI is making a move...")
        ai_move()
        print_board()

        if winner(board, 'O'):
            print("AI wins!")
            break
        if is_full():
            print("It's a tie!")
            break

if __name__ == "__main__":
    play()
