for i in range(int(input())):
    print(x // 10 + (x % 10) // 5 if (x := int(input())) % 5 == 0 else -1)