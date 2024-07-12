for i in range(int(input())):
    x, y, z = map(int, input().split())
    print('YES' if z * 60 * 24 >= x * y else 'NO')