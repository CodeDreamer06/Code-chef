for i in range(int(input())):
    a, b, c, x = map(int, input().split())
    print('YES' if sum((m := sorted([a, b, c]))) - min(m) >= x else 'NO')