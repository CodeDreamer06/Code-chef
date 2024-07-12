for i in range(int(input())):
    n, x, y = map(int, input().split())
    print('YES' if x * y >= n else 'NO')