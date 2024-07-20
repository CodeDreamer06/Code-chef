for i in range(int(input())):
    print(sum((prices := list(map(int, input().split())))) - min(prices))