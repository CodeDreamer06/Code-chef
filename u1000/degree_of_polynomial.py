for i in range(int(input())):
    input()
    coefficients = list(reversed(input().split()))
    for i, v in enumerate(coefficients):
        if v == '0':
            continue
        print(len(coefficients) - i - 1)
        break