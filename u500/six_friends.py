for i in range(int(input())):
    x, y = map(int, input().split())
    print(min(x * 3, y * 2))