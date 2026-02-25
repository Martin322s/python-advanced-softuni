rows, cols = [int(x) for x in input().split(" ")]
matrix = []

for row in range(rows):
    current_row = []
    for col in range(cols):
        first_char = chr(97 + row)
        second_char = chr(97 + row + col)
        palindrome = first_char + second_char + first_char
        current_row.append(palindrome)
    matrix.append(current_row)

print('\n'.join([' '.join(row) for row in matrix]))