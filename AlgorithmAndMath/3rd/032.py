def search_binary(X, A):
    return 'Yes' if X in A else 'No'

def main():
    N, X = map(int, input().split())
    A = map(int, input().split())
    print(search_binary(X, A))

if __name__ == "__main__":
    main()
