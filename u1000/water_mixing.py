for i in range(int(input())):
    a, b, x, y = map(int, input().split())
    print('YES' if (x >= b - a if b > a else y >= a - b) else 'NO')