for i in range(int(input())):
    sample = input().split()
    print(max(0, int(sample[0]) - int(sample[1])))