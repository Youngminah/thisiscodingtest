import copy
n, m = map(int ,input().split())

W = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    a = list(map(int, input().split()))
    W.append(a)


def dfs(x, y, W_copy, n, m, dx, dy, count):
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return 0, W_copy
    if W_copy[x][y] == 0 or W_copy[x][y] == 1 or  W_copy[x][y] == 3:
        return 0, W_copy

    W_copy[x][y] = 3

    for k in range(4):
        i = x + dx[k]
        j = y + dy[k]
        if i < 0 or j < 0 or i >= n or j >= m:
            continue
        if W_copy[i][j] == 0:
            if (i, j) not in count:
                count.append((i, j))

    dfs(x + 1, y, W_copy, n, m, dx, dy, count)
    dfs(x - 1, y, W_copy, n, m, dx, dy, count)
    dfs(x, y + 1, W_copy, n, m, dx, dy, count)
    dfs(x, y - 1, W_copy, n, m, dx, dy, count)
    #print(count)
    return len(count), W_copy


W_copy = copy.deepcopy(W)
total = 0
for i in range(n):
    for j in range(m):
        count = []
        #print(W_copy)
        tmp, W_copy = dfs(i, j, W_copy, n, m, dx, dy, count)
        total += tmp


print(total)

