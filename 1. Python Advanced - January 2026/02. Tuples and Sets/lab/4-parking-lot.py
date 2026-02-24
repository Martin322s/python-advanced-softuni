n = int(input())

parking_lot = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        parking_lot.add(number)
    elif direction == "OUT":
        parking_lot.remove(number)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")