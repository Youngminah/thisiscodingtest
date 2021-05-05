def solution(p):
    answer = recursive(p)
    return answer


def recursive(p):
    if p == "":
        return ""

    l, r = 0, 0
    i = 0

    while True:
        if p[i] == '(':
            l += 1
        else:
            r += 1

        if l == r:
            break
        i += 1

    u = p[0:i + 1]
    v = p[i + 1:]
    print("u->" + u)
    print("v->" + v)

    if isright(u):
        print("aa")
        return u + recursive(v)
    else:
        result = "" + "(" + recursive(v) + ")"
        trim = ""
        for j in range(1, len(u) - 1):
            if u[j] == '(':
                trim += ")"
            else:
                trim += "("

        result += trim
        return result


def isright(s):
    stack = []

    if s[0] != '(':
        return False

    stack.append('(')

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:
            top = stack.pop()
            if top == '(':
                continue
            else:
                return False

    return True



