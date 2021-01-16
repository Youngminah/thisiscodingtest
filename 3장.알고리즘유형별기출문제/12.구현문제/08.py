s = input()
target= []

num = 0
for i in range(len(s)):
    if s[i].isalpha():
        target.append(s[i])
    else:
        num += int(s[i])

target.sort()

print("".join(target), end="")
print(num)
