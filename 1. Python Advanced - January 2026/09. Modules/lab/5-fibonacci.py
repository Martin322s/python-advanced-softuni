from fibonacci import create_sequence, locate_number

sequence = []

while True:
    command = input()

    if command == "Stop":
        break

    parts = command.split()

    if parts[0] == "Create":
        count = int(parts[2])
        sequence = create_sequence(count)
        print(*sequence)

    elif parts[0] == "Locate":
        number = int(parts[1])
        index = locate_number(sequence, number)

        if index != -1:
            print(f"The number - {number} is at index {index}")
        else:
            print(f"The number {number} is not in the sequence")