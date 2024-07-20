for i in range(int(input())):
    x, y = map(int, input().split())
    print(0 if y == x else y // x - 1 if y % x == 0 else y // x)