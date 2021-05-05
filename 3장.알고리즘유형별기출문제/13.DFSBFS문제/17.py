from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0 :
            data.append((graph[i][j], 0, i, j))

s, x, y = map(int, input().split())

data.sort()
queue = deque(data)

def bfs(graph, s, queue):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        virus, ps, px, py = queue.popleft()

        if ps == s:
            break

        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if nx < 0 or ny < 0 or nx >= n or  ny >= n:
                continue

            if graph[nx][ny] != 0:
                continue

            graph[nx][ny] = virus
            queue.append((virus, ps+1, nx, ny))



bfs(graph, s, queue)
print(graph[x-1][y-1])