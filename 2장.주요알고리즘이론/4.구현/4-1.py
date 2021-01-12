N = int(input())

move = list(input().split())


lrud_x =[-1, 1, 0, 0]
lrud_y = [0, 0, -1, 1]


x = 1
y = 1

for i in move:
    if y > 1 and i == 'L':
        y += lrud_x[0]
    elif y < N and i == 'R':
        y += lrud_x[1]
    elif x > 1 and i == 'U':
        x += lrud_y[2]
    elif x < N and i == 'D':
        x += lrud_y[3]


print(str(x)+" "+str(y))



