for i in range(int(input())):
    n = int(input())
    numbers = map(int, input().split())
    print(abs(sum(numbers)) // 2 if n % 2 == 0 else -1)