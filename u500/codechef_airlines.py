for i in range(int(input())):
    x, y, z = map(int, input().split())
    print(z * min(x * 10, y))