for i in range(int(input())):
    x, a, b = map(int, input().split())
    print('Qualify' if a + b * 2 >= x else 'NotQualify')