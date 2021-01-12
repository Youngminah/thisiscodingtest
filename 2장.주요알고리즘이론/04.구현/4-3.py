location = input()

dx = [-2, -2, 2, 2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

x = ord(location[0]) - ord('a')+1
y = int(location[1])

result = 0

for i in range(8):
    nx = x + dx[i]
    ny = x + dy[i]

    if nx > 8 or nx <1 or ny > 8 or ny < 1 :
        continue;

    result += 1

print( result)
