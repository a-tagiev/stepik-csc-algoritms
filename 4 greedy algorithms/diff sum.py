a = int(input())
curr_sum = 0
f = 0
ans = []
cnt = 0
i = 1
while curr_sum < a - 2 * i:
    curr_sum += i
    ans.append(i)
    i += 1
if a - curr_sum != 0 and a-curr_sum not in ans:
    ans.append(a - curr_sum)
    cnt += 1
print(len(ans))
print(*ans)
