from collections import deque

green_time = int(input())
free_window = int(input())

cars = deque()
passed = 0
crash = False

while True:
    command = input()

    if command == "END":
        break

    if command != "green":
        cars.append(command)
        continue

    green_left = green_time

    while cars and green_left > 0:
        car = cars.popleft()
        car_len = len(car)

        if car_len <= green_left:
            green_left -= car_len
            passed += 1
        else:
            time_available = green_left + free_window

            if car_len <= time_available:
                passed += 1
                break
            else:
                hit_index = time_available
                print("A crash happened!")
                print(f"{car} was hit at {car[hit_index]}.")
                crash = True
                break

    if crash:
        break

if not crash:
    print("Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")