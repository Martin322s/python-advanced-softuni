def fill_the_box(height, length, width, *args):
    free_space = height * length * width

    for i in range(len(args)):
        if args[i] == "Finish":
            break

        if free_space >= args[i]:
            free_space -= args[i]
        else:
            cubes_left = args[i] - free_space

            for j in range(i + 1, len(args)):
                if args[j] == "Finish":
                    break
                cubes_left += args[j]

            return f"No more free space! You have {cubes_left} more cubes."

    return f"There is free space in the box. You could put {free_space} more cubes."