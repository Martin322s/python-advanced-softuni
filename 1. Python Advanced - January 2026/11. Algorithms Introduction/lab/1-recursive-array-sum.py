def recursive_array_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + recursive_array_sum(arr, index + 1)


nums = list(map(int, input().split()))
print(recursive_array_sum(nums))