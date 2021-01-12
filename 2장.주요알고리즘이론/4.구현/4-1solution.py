n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]

    if nx> n or nx < 1 or ny > n or ny <0 :
        continue;

    x = nx;
    y = ny;



print(x, y)
