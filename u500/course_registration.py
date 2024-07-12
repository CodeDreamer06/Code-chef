for i in range(int(input())):
    n, m, k = map(int, input().split())
    print('Yes' if n <= m - k else 'No')