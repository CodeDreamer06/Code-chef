for i in range(int(input())):
    a, b, c = map(int, input().split())
    print('YES' if a <= b and c <= b else 'NO')