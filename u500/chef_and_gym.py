for i in range(int(input())):
    x, y, z = map(int, input().split())
    print(2 if z >= x + y else 1 if z >= x else 0)