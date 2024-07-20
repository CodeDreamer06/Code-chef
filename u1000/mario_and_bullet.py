for i in range(int(input())):
    x, y, z = map(int, input().split())
    print(max(0, z - y // x))