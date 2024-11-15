def prime(N):
    primes = [True] * (N+1)
    primes[0] = primes[1] = False
    for i in range(2, int(N**0.5)+1):
        if primes[i]:
            for j in range(i*i, N+1, i):
                primes[j] = False
    return [i for i in range(N+1) if primes[i]]

def main():
    N = int(input())
    print(*prime(N))

if __name__ == "__main__":
    main()
