# def divisor(n):
#     div = set()
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             div.add(i)
#             div.add(n // i)
#     return sorted(div)

# N = int(input())
# print(*divisor(N), sep='\n')

def isPrime(n):
    if n < 2: return False
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False
    for i in range(5, int(n**0.5)+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
N = int(input())
print("Yes" if isPrime(N) else "No")
