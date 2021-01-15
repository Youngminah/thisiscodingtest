def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    a = []

    for i in range(n):
        a.append([food_times[i], i + 1])

    a.sort()
    k = k + 1

    tmp = 0
    m = len(a)
    i = 0
    for i in range(n):
        value = a[i][0] - tmp
        if value * m < k:
            k = k - value * m
            tmp += value
            m -= 1
        else:
            break

    a = sorted(a[i:], key=lambda x: x[1])
    l = len(a)

    if l == 1:
        answer = a[0][1]
    elif l > k:
        answer = a[k - 1][1]
    else:
        answer = a[k % len(a) - 1][1]

    return answer