for i in range(int(input())):
    x, y = map(int, input().split())
    print('YES' if x >= y * 30 else 'NO')