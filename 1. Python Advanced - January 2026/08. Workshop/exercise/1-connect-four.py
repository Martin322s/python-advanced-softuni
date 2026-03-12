class InvalidNumberValueError(Exception):
    pass


class InvalidNumberRangeError(Exception):
    pass


class ColumnFullError(Exception):
    pass


ROWS = 6
COLS = 7
EMPTY = " "


def read_players_data():
    player_one_name = input("Enter the name of Player 1: ")
    player_two_name = input("Enter the name of Player 2: ")

    player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

    while player_one_sign not in ["X", "O"]:
        print("Invalid choice. Please choose either X or O.")
        player_one_sign = input(f"{player_one_name}, choose your sign (X/O): ").upper()

    player_two_sign = "O" if player_one_sign == "X" else "X"

    print(f"{player_one_name} will be '{player_one_sign}' and {player_two_name} will be '{player_two_sign}'.")
    print(f"{player_one_name} starts first.")

    return (player_one_name, player_one_sign), (player_two_name, player_two_sign)


def print_board_numeration():
    print("This is the numeration for Connect Four columns:")
    print(" " + "   ".join(str(i) for i in range(1, COLS + 1)))
    print()


def print_game_board(board):
    print("\n+" + "---+" * COLS)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+" + "---+" * COLS)
    print("  " + "   ".join(str(i) for i in range(1, COLS + 1)))
    print()


def check_position(column, board):
    try:
        column = int(column)
    except ValueError:
        raise InvalidNumberValueError(f"The column must be a number between 1 and {COLS}.")

    if column < 1 or column > COLS:
        raise InvalidNumberRangeError(f"The column must be a number between 1 and {COLS}.")

    col_index = column - 1

    if board[0][col_index] != EMPTY:
        raise ColumnFullError("This column is full. Please choose another one.")

    for row_index in range(ROWS - 1, -1, -1):
        if board[row_index][col_index] == EMPTY:
            return row_index, col_index

    raise ColumnFullError("This column is full. Please choose another one.")


def check_winner(board, sign):
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == sign for i in range(4)):
                return True
            
    for c in range(COLS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == sign for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == sign for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if all(board[r - i][c + i] == sign for i in range(4)):
                return True

    return False


def check_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

player_one_data, player_two_data = read_players_data()
print_board_numeration()
print_game_board(board)

turns = 1

while True:
    current_player_name, current_player_sign = player_one_data if turns % 2 != 0 else player_two_data
    column = input(f"{current_player_name}, choose a column (1-{COLS}) to drop your disc: ")

    try:
        row_index, col_index = check_position(column, board)
    except (InvalidNumberValueError, InvalidNumberRangeError, ColumnFullError) as e:
        print(e)
        continue
    else:
        board[row_index][col_index] = current_player_sign
        print_game_board(board)
        turns += 1

    if check_winner(board, current_player_sign):
        print(f"Congratulations {current_player_name}! You have won the game!")
        break

    if check_draw(board):
        print("The game is a draw!")
        break