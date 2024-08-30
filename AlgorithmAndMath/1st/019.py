def main():
    N = input()
    A = input()
    c = [A.count(c) for c in ('123')]
    # nCr
    c_1 = c[0] * (c[0]-1) // 2
    c_2 = c[1] * (c[1]-1) // 2
    c_3 = c[2] * (c[2]-1) // 2
    print(c_1 + c_2 + c_3)

if __name__ == "__main__":
    main()
