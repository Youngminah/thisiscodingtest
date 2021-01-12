location = input()

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1),(2,1), (1,2),(-1,2), (-2,1)]

x = ord(location[0]) - ord('a')+1
y = int(location[1])

result = 0

for step in steps:
    nx = x + step[0]
    ny = x + step[1]

    if nx > 8 or nx <1 or ny > 8 or ny < 1 :
        continue;

    result += 1

print(result)
