s = input()
n = len(s)//2

c1 = 0
c2 = 0
for i in range(n):
    c1 += int(s[i])
    c2 += int(s[n+i])

if c1 == c2:
    print("LUCKY")
else:
    print("READY")