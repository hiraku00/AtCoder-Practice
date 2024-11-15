def factorial(N):
    res = 1
    for i in range(1, N+1):
        res *= i
    return res

def main():
    N = int(input())
    print(factorial(N))

if __name__ == "__main__":
    main()
