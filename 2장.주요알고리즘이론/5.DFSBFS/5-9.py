from collections import deque

def bfs(x, queue, visited):
    queue.append(1)
    visited[1] = True
    while queue :
        tmp = queue.popleft()
        print(tmp, end=" ")
        for i in graph[tmp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

queue = deque()

visited = [False]*9

graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

bfs(1,queue,visited)