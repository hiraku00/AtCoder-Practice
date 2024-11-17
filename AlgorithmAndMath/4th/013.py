def divisor(N):
    div = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            div.append(i)
            if i != N // i:
                div.append(N // i)
    return sorted(div)

def main():
    N = int(input())
    print(*divisor(N), sep='\n')

if __name__ == "__main__":
    main()
