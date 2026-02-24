first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + ' ' + second_command

    if command == 'Add First':
        first_set.update(int(x) for x in data)
    elif command == 'Add Second':
        second_set.update(int(x) for x in data)
    elif command == 'Remove First':
        first_set.difference_update(int(x) for x in data)
    elif command == 'Remove Second':
        second_set.difference_update(int(x) for x in data)
    elif command == 'Check Subset':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

print(', '.join(str(x) for x in sorted(first_set)))
print(', '.join(str(x) for x in sorted(second_set)))