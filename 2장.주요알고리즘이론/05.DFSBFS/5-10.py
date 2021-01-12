n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input())))

def dfs(x, y, a):
    if x >= 0 and y >= 0 and x < n and y < m :
        if a[x][y] == 1:
            return False

        a[x][y] = 1
        dfs(x - 1, y, a)
        dfs(x + 1, y, a)
        dfs(x, y - 1, a)
        dfs(x, y + 1, a)
    return True

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j, a):
            count += 1

print(count)
