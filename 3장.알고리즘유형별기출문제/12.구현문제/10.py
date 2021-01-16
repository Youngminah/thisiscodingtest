def solution(key, lock):
    m = len(key)
    n = len(lock)
    K = 2 * (m - 1) + n
    total_map = [[-1] * (K) for _ in range(K)]
    count = 0
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 1:
                count += 1
            total_map[m - 1 + i][m - 1 + j] = lock[i][j]

    target = n * n
    for _ in range(4):
        i = 0
        while i + m <= K:
            j = 0
            while j + m <= K:
                block = count
                for x in range(m):
                    for y in range(m):
                        if total_map[i + x][j + y] == -1:
                            continue
                        if total_map[i + x][j + y] == 1 and key[x][y] == 1:
                            break
                        if total_map[i + x][j + y] == 0 and key[x][y] == 1:
                            block += 1

                if block == target:
                    return True
                j += 1
            i += 1
        print(key)
        key = rotation(key, m)
    return False

def rotation(key, m):
    array = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            array[j][m - 1 - i] = key[i][j]
    return array