for i in range(int(input())):
    print('BRONZE' if (donations := int(input())) <= 3 else 'SILVER' if donations <= 6 else 'GOLD')