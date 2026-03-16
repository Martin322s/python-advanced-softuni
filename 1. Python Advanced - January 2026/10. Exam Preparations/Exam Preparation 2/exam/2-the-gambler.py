def is_in_boundries(row, col, size):
    return 0 <= row < size and 0 <= col < size

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())

board = []
player_position = None

for row_index in range(n):
    data = list(input())

    if "G" in data:
        player_position = (row_index, data.index("G"))

    board.append(data)

direction = input()
money = 100

while direction != "end":
    current_row_index, current_col_index = player_position
    row_movement, col_movement = direction_mapper[direction]
    desired_row = current_row_index + row_movement
    desired_col = current_col_index + col_movement

    if not is_in_boundries(desired_row, desired_col, n):
        print("Game over! You lost everything!")
        exit()

    symbol = board[desired_row][desired_col]
    board[desired_row][desired_col] = "G"
    board[current_row_index][current_col_index] = "-"
    player_position = (desired_row, desired_col)

    if symbol == "W":
        money += 100
    elif symbol == "P":
        money -= 200

        if money < 0:
            money = 0
            print("Game over! You lost everything!")
            exit()
    elif symbol == "J":
        money += 100000
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        print('\n'.join(''.join(row) for row in board))
        exit()


    direction = input()

print(f"End of the game. Total amount: {money}$")
print('\n'.join(''.join(row) for row in board))