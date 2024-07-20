for i in range(int(input())):
    print('NORMAL' if (r := int(input()) % 3) == 0 else 'SMALL' if r == 2 else 'HUGE')