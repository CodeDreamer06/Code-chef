for i in range(int(input())):
    print((x := int(input())) - (0 if x <= 100 else 25 if x <= 1000 else 100 if x <= 5000 else 500))