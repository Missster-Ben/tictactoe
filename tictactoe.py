def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def get_valid_move(board):
    while True:
        move = input("Enter your move (e.g., A1, B2): ").strip().upper()
        if len(move) != 2 or move[0] not in "ABC" or move[1] not in "123":
            print("Invalid input. Please use the format 'A1', 'B2', etc.")
        else:
            row = ord(move[0]) - ord('A')
            col = int(move[1]) - 1
            if board[row][col] == ' ':
                return row, col
            else:
                print("That cell is already taken. Try again.")

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    print("Welcome to ASCII Tic-Tac-Toe!")

    while True:
        print_board(board)
        row, col = get_valid_move(board)
        board[row][col] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
