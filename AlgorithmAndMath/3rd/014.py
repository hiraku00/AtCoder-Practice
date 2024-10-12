def prime_fractorization(N):
    fractors = []
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            fractors.append(i)
            N //= i
    if N > 1:
        fractors.append(N)
    return fractors

def main():
    N = int(input())
    print(' '.join(map(str, prime_fractorization(N))))

if __name__ == "__main__":
    main()
