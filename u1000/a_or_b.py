for i in range(int(input())):
    x, y = map(int, input().split())
    print(1500 - 2 * min(3 * x + 2 * y, x + 3 * y))