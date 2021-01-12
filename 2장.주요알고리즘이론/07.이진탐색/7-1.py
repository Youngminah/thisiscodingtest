n, target = input().split()
n = int(n)

a   = list(input().split())

def sequential_search(target, n, a):
    for i in range(n) :
        if a[i] == target:
            return i+1

print(sequential_search(target,n,a))

