def dfs(x,graph):
    print(x, end = " ")
    for i in graph[x]:
        if visited[i] == True :
            continue
        visited[i] = True
        dfs(i,graph)

graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]


visited = [False]*9
visited[1]=True
dfs(1,graph)
