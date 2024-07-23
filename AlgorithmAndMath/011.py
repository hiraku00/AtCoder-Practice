def isPrime(n):
    if n < 2: return False
    if n == 2 or n ==3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

N = int(input())
ans = []
for i in range(2, N):
    if isPrime(i):
        ans.append(i)
print(*ans)
