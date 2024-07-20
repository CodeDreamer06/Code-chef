for i in range(int(input())):
    x, y, a, b = map(int, input().split())
    print(2 - sum(i in (x, y) for i in (a, b)))