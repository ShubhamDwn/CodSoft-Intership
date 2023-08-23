import math

# The Tic-Tac-Toe board is represented as a 3x3 list
# 'X' represents the human player, 'O' represents the AI player, and None represents an empty cell
initial_board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

# Function to check if a player has won the game
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell is not None for cell in row) for row in board)

# Minimax algorithm with Alpha-Beta Pruning
def minimax_alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = None
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    eval = minimax_alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = None
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function for AI player to make a move
def ai_move(board):
    best_move = None
    best_eval = -math.inf
    alpha = -math.inf
    beta = math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'O'
                eval = minimax_alpha_beta(board, 0, alpha, beta, False)
                board[i][j] = None
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Function to print the current state of the board
def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 9)

# Main game loop
def play_game():
    current_board = initial_board
    while not is_board_full(current_board) and not check_winner(current_board, 'X') and not check_winner(current_board, 'O'):
        print_board(current_board)
        row, col = map(int, input("Enter your move [row and column, (0 to 2)]: ").split())
        if current_board[row][col] is not None:
            print("Cell is already occupied. Try again.")
            continue
        current_board[row][col] = 'X'
        
        if is_board_full(current_board) or check_winner(current_board, 'X') or check_winner(current_board, 'O'):
            break
        print("\n")
        print("AI is thinking...")
        print("\n")
        ai_row, ai_col = ai_move(current_board)
        current_board[ai_row][ai_col] = 'O'
    
    print_board(current_board)
    if check_winner(current_board, 'X'):
        print("You win!")
    elif check_winner(current_board, 'O'):
        print("AI wins!")
    else:
        print("It's a draw!")

# Start the game
play_game()