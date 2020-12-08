from collections import deque

n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int,input())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
queue =deque()
count = 1
visited =[]

def bfs(count , x,y):
    queue.append((x,y))
    a[x][y]=1

    while queue:
        v = queue.popleft()
        visited.append(v)
        (x,y)=v
        count = a[x][y]+1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m and a[nx][ny] !=0 and (nx,ny) not in visited:
                a[nx][ny] = count
                queue.append((nx,ny))

    return a[n-1][m-1]

print(bfs(count,0,0))
