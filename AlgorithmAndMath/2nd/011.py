def prime(N):
    primes = [True] * (N+1)
    primes[0] = primes[1] = False
    p = 2
    while p*p <= N:
        if primes[p]:
            for i in range(p*p, N+1, p):
                primes[i] = False
        p += 1
    return [i for i in range(N+1) if primes[i]]

def main():
    N = int(input())
    print(*prime(N))

if  __name__ == "__main__":
    main()
