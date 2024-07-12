for i in range(int(input())):
    x, y = map(int, input().split())
    print('YES' if y <= 1.07 * x else 'NO')