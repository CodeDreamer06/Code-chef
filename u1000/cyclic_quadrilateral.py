for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    print('YES' if a + c == b + d == 180 else 'NO')