def display_board(board):
    """Display the Tic Tac Toe board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def player_input(player, board):
    """Ask the player to choose a position"""
    while True:
        try:
            pos = int(input(f"Player {player}, choose your position (1-9): "))
            if pos < 1 or pos > 9:
                print("❌ Invalid position! Choose a number from 1 to 9.")
            elif board[pos - 1] != " ":
                print("❌ Position already taken! Choose another one.")
            else:
                return pos - 1
        except ValueError:
            print("❌ Invalid input! Enter a number from 1 to 9.")


def check_win(board, player):
    """Check if the player has won"""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def is_board_full(board):
    """Check if the board is full"""
    return all(cell != " " for cell in board)


def play():
    """Main function to play the game"""
    board = [" "] * 9  # initialize empty board
    current_player = "X"  # X starts first

    print("Welcome to Tic Tac Toe!")
    display_board(board)

    while True:
        position = player_input(current_player, board)
        board[position] = current_player
        display_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_board_full(board):
            print("🤝 It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play()
