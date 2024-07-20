for i in range(int(input())):
    a, b = map(int, input().split())
    print(c if 0 < (c := 21 - a - b) < 11 else -1)