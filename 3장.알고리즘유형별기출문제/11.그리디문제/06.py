def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    n = len(food_times)
    a = []

    for i in range(n):
        a.append([food_times[i], i + 1])

    a.sort()
    k = k + 1

    for i in range(n):
        m = len(a)
        value = a[0][0]
        if value * m < k:
            k = k - value * m
            a.pop(0)
            for i in range(len(a)):
                a[i][0] -= value
        else:
            break

    a.sort(key=lambda x: x[1])

    if len(a) == 1:
        answer = a[0][1]
    elif len(a) > k:
        answer = a[k - 1][1]
    else:
        answer = a[k % len(a) - 1][1]

    return answer