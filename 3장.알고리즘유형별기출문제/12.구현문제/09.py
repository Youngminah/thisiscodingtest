def solution(s):
    n = len(s)
    if n == 1:
        return 1

    half_N = n // 2
    total = []
    for i in range(1, half_N + 1):
        result = []
        target = s[:i]
        rest = s[i:]
        count = 1
        j = 0
        while len(target) > 0:
            if target == rest[j:j + i]:
                count += 1
                j += i
            else:
                result.append((count, target))
                count = 1
                target = rest[j:j + i]
                rest = rest[j + i:]
                j = 0

        tmp = ""
        for data in result:
            if data[0] != 1:
                tmp = tmp + str(data[0])
            tmp = tmp + data[1]
        total.append(tmp)

    answer = 10001
    for data in total:
        if len(data) < answer:
            answer = len(data)

    return answer