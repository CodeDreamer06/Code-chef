for i in range(int(input())):
    print('Upper' if (n := int(input())) > 15 else 'Lower', 'Double' if n < 11 or 15 < n < 26 else 'Single')