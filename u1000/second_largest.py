from heapq import nlargest
for i in range(int(input())):
    print(nlargest(2, map(int, input().split()))[1])