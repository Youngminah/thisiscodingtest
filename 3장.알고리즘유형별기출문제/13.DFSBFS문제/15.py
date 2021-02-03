from collections import deque
import sys

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


visit = [False] * (n+1)
queue = deque()
count = 0
result = []

def bfs(start, graph, count,result):
    visit[start] = True
    queue.append((start,count))
    while queue:
        #print(queue)
        temp, count = queue.popleft()
        for i in graph[temp]:
            if visit[i] :
                continue
            if count+1 == k:
                result.append(i)
            visit[i] = True
            queue.append((i,count+1))

bfs(x, graph, count, result)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)

