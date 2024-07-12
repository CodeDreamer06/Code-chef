for i in range(int(input())):
    print(0 if (speed := int(input())) <= 70 else 500 if speed <= 100 else 2000)