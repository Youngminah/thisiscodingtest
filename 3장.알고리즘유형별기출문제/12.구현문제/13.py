#1: 15: 00
from itertools import combinations
import heapq

n, m = map(int, input().split())
city_info = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    city_info.append(tmp)

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city_info[i][j] == 2 :
            chicken.append([i+1 , j+1])
        elif city_info[i][j] == 1:
            house.append([i+1, j+1])

chicken_list = list(combinations(chicken, m))
heap = []
for k in range(len(chicken_list)):
    total = 0
    for i in range(len(house)):
        short = n*n
        for j in range(len(chicken_list[k])):
            tmp = abs(house[i][0] - chicken_list[k][j][0]) + abs(house[i][1] - chicken_list[k][j][1])
            if short > tmp:
                short = tmp
        total += short
    heapq.heappush(heap, total)

print(heap[0])




