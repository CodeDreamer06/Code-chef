for i in range(int(input())):
    x, y, z = map(int, input().split())
    print('YES' if z / (x * y) > 0.5 else 'NO')