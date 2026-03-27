import math

# Initialize the board with empty spaces
board = [' ' for _ in range(9)]

def print_board():
    """Displays the 3x3 board in a user-friendly format."""
    print("\n")
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(state, player):
    """Returns True if the specified player has a winning combination."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(state[i] == player for i in combo) for combo in win_conditions)

def is_draw(state):
    """Returns True if no more moves are possible and there is no winner."""
    return ' ' not in state

def minimax(state, depth, is_maximizing):
    """Minimax algorithm to find the optimal move for the AI."""
    if check_winner(state, 'O'): return 1
    if check_winner(state, 'X'): return -1
    if is_draw(state): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if state[i] == ' ':
                state[i] = 'O'
                score = minimax(state, depth + 1, False)
                state[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if state[i] == ' ':
                state[i] = 'X'
                score = minimax(state, depth + 1, True)
                state[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move():
    """AI calculates the best available move using Minimax."""
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# --- Main Gameplay Loop ---
print("--- Tic-Tac-Toe AI (Unbeatable) ---")
print("Positions are marked 1 through 9.")
print_board()

while True:
    # Human Player Turn
    try:
        user_input = int(input("Enter your move (1-9): "))
        
        # Validation: Only allow numbers 1-9 and check if spot is empty
        if user_input < 1 or user_input > 9:
            print("Invalid range! Please choose a number between 1 and 9.")
            continue
        
        move = user_input - 1 # Convert 1-9 range to 0-8 index
        
        if board[move] != ' ':
            print("That spot is already taken! Try again.")
            continue
            
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    board[move] = 'X'
    
    if check_winner(board, 'X'):
        print_board()
        print("Amazing! You beat the AI.")
        break
    if is_draw(board):
        print_board()
        print("It's a draw!")
        break

    # AI Player Turn
    print("AI is making its move...")
    ai_move = get_best_move()
    board[ai_move] = 'O'
    print_board()

    if check_winner(board, 'O'):
        print("AI wins! Better luck next time.")
        break
    if is_draw(board):
        print("It's a draw!")
        break