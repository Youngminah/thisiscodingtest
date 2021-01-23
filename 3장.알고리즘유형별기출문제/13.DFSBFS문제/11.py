n = int(input())
k = int(input())

m = [[-1]*n for _ in range(n)]
m[0][0] = 0
location = []
location.append((0,0))

for _ in range(k):
    a, b = map(int, input().split())
    m[a-1][b-1] = 1

l = int(input())
snake = []
sec = 0

for _ in range(l):
    tmp = list(input().split())
    snake.append(tmp)

rows = [0, 1, 0, -1]
cols = [1, 0,-1, 0]

head = 0
row , col = 0, 0
while True:
    sec += 1
    row += rows[head%4]
    col += cols[head%4]

    if row >= n or col >= n or row < 0 or col < 0 :
        break
    if m[row][col] == 0:
        break

    if m[row][col] == -1:
        a, b = location.pop(0)
        m[a][b] = -1

    m[row][col] = 0
    location.append((row, col))

    if len(snake) != 0 and sec == int(snake[0][0]):
        if snake[0][1] == 'D':
            head += 1
        else:
            head -= 1
        snake.pop(0)

print(sec)