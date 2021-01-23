# 2:00:00
import copy

def solution(n, build_frame):
    up = [[0] * (n + 1) for _ in range(n + 1)]
    side = [[0] * (n + 1) for _ in range(n + 1)]
    result = []

    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b == 1:
            if a == 0:
                if isAvailOfUp(x, y, n, up, side):
                    up[x][y] = 1
                    result.append([x, y, a])
            else:
                if isAvailOfSide(x, y, n, up, side):
                    side[x][y] = 1
                    result.append([x, y, a])
        else:
            up_copy = copy.deepcopy(up)
            side_copy = copy.deepcopy(side)
            if a == 0:
                up_copy[x][y] = 0
            else:
                side_copy[x][y] = 0

            decision = True
            for data in result:
                tmp1, tmp2, tmp3 = data
                if data == [x, y, a]:
                    continue
                if tmp3 == 0:
                    if not isAvailOfUp(tmp1, tmp2, n, up_copy, side_copy):
                        decision = False
                        break
                else:
                    if not isAvailOfSide(tmp1, tmp2, n, up_copy, side_copy):
                        decision = False
                        break
            if decision:
                result.remove([x, y, a])
                up = up_copy
                side = side_copy

    result = sorted(result, key=lambda x: (x[0], x[1], x[2]))
    return result

def isAvailOfUp(x, y, n, up_copy, side_copy):
    answer = False
    if y == 0:
        return True
    if y != 0 and up_copy[x][y - 1] == 1:
        return True
    if side_copy[x][y] == 1:
        return True
    if x != 0 and side_copy[x - 1][y] == 1:
        return True
    return answer

def isAvailOfSide(x, y, n, up_copy, side_copy):
    answer = False
    if y != 0 and up_copy[x][y - 1] == 1:
        return True
    if y != 0 and x < n and up_copy[x + 1][y - 1] == 1:
        return True
    if x != 0 and side_copy[x - 1][y] == 1 and x < n and side_copy[x + 1][y] == 1:
        return True
    return answer