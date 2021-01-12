n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0


for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

last , mid = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])



result = graph[1][mid] + graph[mid][last]
if result<INF:
    print(result)
else:
    print(-1)

