from collections import deque
import copy
import sys
input = sys.stdin.readline

def infection(graph, next, j, z, n, w):
    queue = deque()
    queue.append((j,z))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        j, z = queue.popleft()

        for i in range(4):
            nx = j + dx[i]
            ny = z + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] != 0:
                continue

            graph[nx][ny] = graph[j][z]
            next[w].append((nx,ny))

    return graph, next

n, k = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())


virus = [[] for _ in range(k + 1)]
for j in range(n):
    for z in range(n):
        if graph[j][z] != 0 :
            virus[graph[j][z]].append((j, z))

for _ in range(s):

    next = [[] for _ in range(k + 1)]
    for w in range(1, k+1):
        for data in virus[w]:
            j, z = data
            graph, next = infection(graph, next, j, z, n, w)

    virus = next
print(graph[x-1][y-1])
#print(graph)
