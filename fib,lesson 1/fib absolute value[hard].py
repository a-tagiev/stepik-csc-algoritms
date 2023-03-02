def fib(n, m, count=0):
    arr = []
    if n <= 1:
        return 1
    arr.append(0)
    arr.append(1)
    for i in range(2, n + 1):
        arr.append((arr[i - 1] + arr[i - 2]) % m)
        if count == 1:
            return arr[n % (len(arr) - 3)]
        if arr[i - 1] == 0 and arr[i] == 1:
            count += 1
    return arr[-1]


def main():
    n, m = map(int, input().split())
    print(fib(n, m))


if __name__ == "__main__":
    main()