n, m = map(int, input().split())

x, y, h = map(int, input().split())

map1 = []

for i in range(n):
    map1.append(list(map(int, input().split())))


isavail = [(-1, 0), (0,1), (1,0), (0,-1)]

map1[x][y] = 1


count = 0
result = 1

while True:
    if h == 0 :
        h = 3
    else :
        h -= 1


    nx = x + isavail[h][0]
    ny = y + isavail[h][1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m or map1[nx][ny] == 1:
        count += 1
        if count == 5:
            break
        continue

    x = nx
    y = ny
    map1[x][y] = 1
    result += 1
    count = 0

print(result)

