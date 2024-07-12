for i in range(int(input())):
    print('Yes' if 2 * max((companies := list(map(int, input().split())))) > sum(companies) else 'No')