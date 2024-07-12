for i in range(int(input())):
    print('MILD' if (level := int(input())) < 4 else 'MEDIUM' if level < 7 else 'HOT')