for i in range(int(input())):
    r = list(map(int, input().split()))
    print('Alice' if (condition := sum(r[:3]) - sum(r[3:]) - min(r[:3]) + min(r[3:])) > 0 else 'Bob' if condition < 0 else 'Tie')