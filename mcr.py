def is_win(game):
    """
    Check if there is a winner in the Tic-Tac-Toe game.
    :param game: 2D list representing the game board
    :return: True if there is a winner, False otherwise
    """
    # Check rows and columns
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] in ('X', 'O'):
            return True
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] in ('X', 'O'):
            return True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] in ('X', 'O'):
        return True
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] in ('X', 'O'):
        return True
    return False


def print_board(game):
    """
    Print the current state of the Tic-Tac-Toe board.
    :param game: 2D list representing the game board
    """
    print("\nGame Board:")
    for row in game:
        print(" | ".join(row))
        print("-" * 5)


def main():
    """
    Main function to play the Tic-Tac-Toe game.
    """
    # Initialize game board
    game = [[' ' for _ in range(3)] for _ in range(3)]
    player_symbols = ['X', 'O']
    turn = 0  # 0 for Player 1, 1 for Player 2

    print("Welcome to Tic-Tac-Toe!")
    print("Player 1: X")
    print("Player 2: O")
    
    for move_count in range(9):  # Maximum 9 moves
        print_board(game)
        current_player = f"Player {turn + 1}"
        symbol = player_symbols[turn]
        print(f"{current_player}'s turn ({symbol}). Enter cell i:[1..3], j:[1..3]:")
        
        while True:
            try:
                i, j = map(int, input().split())
                if not (1 <= i <= 3 and 1 <= j <= 3):
                    raise ValueError("Input out of range. Try again.")
                i, j = i - 1, j - 1  # Convert to 0-based indexing
                if game[i][j] != ' ':
                    raise ValueError("Cell already occupied. Try again.")
                break
            except ValueError as e:
                print(e)
        
        # Mark the cell
        game[i][j] = symbol
        
        # Check for a win
        if is_win(game):
            print_board(game)
            print(f"Congratulations, {current_player}! You win!")
            return
        
        # Switch turns
        turn = 1 - turn

    # If loop completes, it's a tie
    print_board(game)
    print("It's a tie!")


if __name__ == "__main__":
    main()
