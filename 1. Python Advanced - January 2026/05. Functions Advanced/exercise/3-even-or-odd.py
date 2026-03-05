def even_odd(*args: int):
    nums = list(args)
    command = nums.pop()
    if command.lower() == "even":
        return [el for el in nums if el % 2 == 0]
    elif command.lower() == "odd":
        return [el for el in nums if el % 2 != 0]
    
print(even_odd(1, 2, 3, 4, 5, 6, "even"))