for i in range(int(input())):
    print('LIGHT' if (gauge := int(input())) < 3 else 'MODERATE' if gauge < 7 else 'HEAVY')