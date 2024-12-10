def f(x):
    return x * (x + 1) // 2

def sum_of_divisors(N):
    res = 0
    for i in range(1, int(N**0.5)+1):
        print(f'==================================================== i : {i}')
        print(f'i * i   : {i * i}')
        print(f'2 * i   : {2 * i}')
        print(f'f({N}//{i}) : {f(N//i)}')
        print(f'f({i})    : {f(i)}')
        print(f'(i * i) + (2 * i *(f(N//i) - f(i))) : {(i * i) + (2 * i *(f(N//i) - f(i)))}')
        res += (i * i) + (2 * i *(f(N//i) - f(i)))
        print(f'res : {res}')
    return res

def main():
    N = int(input())
    print(sum_of_divisors(N))

if __name__ == "__main__":
    main()
