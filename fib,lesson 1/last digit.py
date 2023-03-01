def fib(n):
    if n==0:
        return 0
    arr =[0]*(n+1)
    arr[0] = 0
    arr[1]=1
    if n>=2:
        for i in range(2, n+1):
            arr[i] = (arr[i - 1] + arr[i - 2])%10
    return arr[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()