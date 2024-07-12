for i in range(int(input())):
    n, x, k = map(int, input().split())
    print('YES' if k >= x * n else 'NO')