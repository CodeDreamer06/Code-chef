for i in range(int(input())):
    a, b, c = map(int, input().split())
    print('YES' if (a + b) / 2 > c else 'NO')