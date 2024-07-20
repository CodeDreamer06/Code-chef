for i in range(int(input())):
    n, s = int(input()), input().split()
    print((k := sum(i.startswith('S') for i in s)), n - k)