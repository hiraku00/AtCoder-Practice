# simple ver(slow)
def fibonacchi_mod(n):
    MOD = 10**9 + 7
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a+b) % MOD
        # print(a, b)
    return a

def main():
    N = int(input())
    print(fibonacchi_mod(N))

if __name__ == "__main__":
    main()
