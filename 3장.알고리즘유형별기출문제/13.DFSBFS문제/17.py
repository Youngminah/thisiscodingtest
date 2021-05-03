from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))


data.sort()
q = deque(data)
print(q)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, ps, px, py = q.popleft()

    if ps == s:
        break

    for i in range(4):
        nx = n + dx[i]
        ny = n + dy[i]
        
        if nx < 0 or ny < 0 or nx>=n or ny >=n:
            continue

        if graph[ny][ny] != 0 :
            continue

        graph[nx][ny] = virus
        q.append((virus, s+1, nx, ny))

print(graph[x-1][y-1])
