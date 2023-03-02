import random


def quick_sort(arr: list, left: int, right: int):
    if left >= right: return
    ind = random.randrange(left, right)
    i = left
    j = right
    while i <= j:
        while arr[i] < arr[ind]: i += 1
        while arr[ind] < arr[j]: j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    quick_sort(arr, left, j)
    quick_sort(arr, i, right)
    return arr


arr = [int(i) for i in input().split()]
print(*quick_sort(arr, 0, len(arr) - 1))
