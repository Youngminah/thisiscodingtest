import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
start = c
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dijstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue

        for i in graph[now]:
            cost =  dist  + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

count =0
value=0
for i in distance:
    if i != INF:
        count += 1
        value = max( value, i)

print(count-1, value)
