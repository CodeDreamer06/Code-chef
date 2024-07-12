for i in range(int(input())):
    x, y = map(int, input().split())
    print('REPAIR' if x < y else 'NEW PHONE' if x > y else 'ANY')