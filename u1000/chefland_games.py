for i in range(int(input())):
    print('IN' if all(x == '0' for x in input().split()) else 'OUT')