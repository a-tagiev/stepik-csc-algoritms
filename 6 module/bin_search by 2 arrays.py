def bin_search(arr, g):
    left = 0
    r = len(arr) - 1
    while left <= r:
        mid = (left + r) // 2
        if arr[mid] == g:
            return mid + 1
        if arr[mid] > g:
            r = mid - 1
        elif arr[mid] < g:
            left = mid + 1
    return -1


n, *arr = map(int, input().split())
k, *arr2 = map(int, input().split())
ans = [*(bin_search(arr, i) for i in arr2)]
print(*ans)
