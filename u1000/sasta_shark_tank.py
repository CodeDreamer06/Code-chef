for i in range(int(input())):
    a, b = map(int, input().split())
    print('FIRST' if a * 10 > b * 5 else 'SECOND' if a * 10 < b * 5 else 'ANY')