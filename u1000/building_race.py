for i in range(int(input())):
    a, b, x, y = map(int, input().split())
    print('Chef' if x * b > y * a else 'Chefina' if x * b < y * a else 'Both')