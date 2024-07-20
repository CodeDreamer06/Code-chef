for i in range(int(input())):
    n, x, y = map(int, input().split())
    print('YES' if y / x <= n and (y / x).is_integer() else 'NO')