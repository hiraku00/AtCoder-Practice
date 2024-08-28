def fib(n):
    MOD = 10**9+7
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a+b) % MOD
    return a

def main():
    N = int(input())
    print(fib(N))

if __name__ == "__main__":
    main()
