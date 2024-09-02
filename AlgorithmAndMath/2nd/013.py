def divisor(n):
    div = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.add(i)
            div.add(n // i)
    return sorted(div)

def main():
    N = int(input())
    print(*divisor(N), sep='\n')

if __name__ == "__main__":
    main()
