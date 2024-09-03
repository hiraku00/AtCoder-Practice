# same as 011.py
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

def prime_fractorization(n, primes):
    fractors = []
    for i in primes:
        if i * i > n:
            break
        while n % i == 0:
            fractors.append(i)
            n //= i
    if n > 1:
        fractors.append(n)
    return fractors

def main():
    N = int(input())
    primes = prime(N)
    print(*prime_fractorization(N, primes))

if __name__ == "__main__":
    main()
