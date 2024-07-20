for i in range(int(input())):
    p, q = map(int, input().split())
    print('Alice' if (p + q) % 4 in (0, 1) else 'Bob')