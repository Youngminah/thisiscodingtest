#아이디어 모르겠음..

# 9:53 시작.
from itertools import combinations
from itertools import permutations
import math


def solution(n, weak, dist):
    w_n, d_n = len(weak), len(dist)

    for i in range(w_n):
        weak.append(n + weak[i])

    for i in range(w_n):
        dist_all = list(permutations(dist, d_n))

        for j in range(len(dist_all)):
            index = 0
            total = weak[i] + dist_all[index]
            friend = 0
            for k in range(i, i + w_n):
                if total < weak[k]:
                    friend += 1
                    index += 1
                    if index >= len(dist):
                        break
                    total = weak[k] + dist_all[index]

    answer = -1
    return answer

