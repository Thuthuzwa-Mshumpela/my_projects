def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    for _ in range(9):
        while True:
            try:
                row = int(input(f"Player {player}, enter the row (0-2): "))
                col = int(input(f"Player {player}, enter the column (0-2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Please Enter numbers for row and column.")
        
        board[row][col] = player
        print_board(board)
        
        if check_win(board, player):
            print(f"Player {player} wins!")
            break
        if is_full(board):
            print("It's a draw")
            break
        
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
