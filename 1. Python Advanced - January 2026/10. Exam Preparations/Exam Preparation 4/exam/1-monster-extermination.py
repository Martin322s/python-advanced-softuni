from collections import deque

first_numbers_sequence = [int(x) for x in input().split(',')]
second_number_sequence = [int(x) for x in input().split(',')]

monsters_armor_queue = deque(first_numbers_sequence)
solider_strike_impact = second_number_sequence

killed_monsters_count = 0

while monsters_armor_queue and solider_strike_impact:
    monster = monsters_armor_queue.popleft()
    solider = solider_strike_impact.pop()
    result = 0

    if solider >= monster:
        result = solider - monster

        if solider_strike_impact and result != 0:
            solider_strike_impact[-1] += result
        elif not solider_strike_impact and result != 0:
            solider_strike_impact.append(result)
            result = 0
        
        killed_monsters_count += 1
    else:
        result = monster - solider
        monsters_armor_queue.append(result)
        result = 0

if not monsters_armor_queue:
    print("All monsters have been killed!")

if not solider_strike_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters_count}")