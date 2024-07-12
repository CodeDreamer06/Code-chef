for i in range(int(input())):
    x, y = map(int, input().split())
    print('FIRST' if x < y else 'SECOND' if x > y else 'ANY')