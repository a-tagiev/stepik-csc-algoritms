def max_sum(n, a):
    dp = [0] * (n)
    if n == 1:
        return a[0]
    dp[0], dp[1] = a[0], max(a[0] + a[1], a[1])
    if n == 2:
        return dp[1]
    for i in range(3, n + 1):
        dp[i - 1] = max(dp[i - 2], dp[i - 3]) + a[i - 1]
    return dp[n - 1]


n = int(input())
a = list(map(int, input().split()))
print(max_sum(n, a))
