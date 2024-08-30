def f(x):
    return x*(x+1) // 2

def sum_of_divisors(N):
    res = 0
    for i in range(1, int(N**0.5)+1):
        res += i * i + 2 * i * (f(N//i) - f(i))
    return res

def main():
    N = int(input())
    print(sum_of_divisors(N))

if __name__ == "__main__":
    main()
