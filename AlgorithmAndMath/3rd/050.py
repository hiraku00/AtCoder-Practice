def mod_pow(a, b):
    MOD = 10**9+7
    res = 1
    while b > 0:
        print(f'b % 2: {b} % 2 => {b % 2}')
        if b % 2 == 1:
            res = (res * a) % MOD
            print(f'a : {a}')
        a = (a * a) % MOD
        print(f'res : {res}')
        b //= 2
        print(f'b : {b}')
        print(f'---------------')
    return res

def main():
    a, b = map(int, input().split())
    print(mod_pow(a, b))

if __name__ == "__main__":
    main()
