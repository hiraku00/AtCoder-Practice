def modulo_100():
    return sum(map(int, input().split())) % 100

def main():
    _ = int(input())
    print(modulo_100())

if __name__ == "__main__":
    main()
