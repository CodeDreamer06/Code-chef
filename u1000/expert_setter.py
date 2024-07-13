for i in range(int(input())):
    x, y = map(int, input().split())
    print('YES' if y / x >= 0.5 else 'NO')