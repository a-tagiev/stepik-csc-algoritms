a = int(input())
arr = [int(i) for i in input().split()]
arr1 = [0] * (max(arr) + 1)
ans = []
for i in arr:
    arr1[i] += 1
for i in range(max(arr) + 1):
    if arr1[i] != 0:
        for j in range(arr1[i]):
            ans.append(i)
print(*ans)
