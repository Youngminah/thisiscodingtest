def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)

    if(a<b):
        parent[b] = a
    else:
        parent[a] =b

v, e = map(int, input().split())
parent = [0] * (v+1)
cycle = False

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a , b = map(int , input().split())
    if parent[a] == parent[b]:
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle :
    print("사이클이 있음")

else:
    print("사이클 없음")