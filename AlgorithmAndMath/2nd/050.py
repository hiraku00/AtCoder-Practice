def mod_pow(a, b):
    MOD = 10**9 + 7
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return res

def main():
    a, b = map(int, input().split())
    print(mod_pow(a, b))

if __name__ == "__main__":
    main()
