n, m = map(int, input().split())
a = list(map(int,input().split()))

def binary(array, start, end, target):
    if start > end :
        return end

    mid = (start+end)//2
    result =0

    for i in array:
        if (i - mid) > 0 :
            result += i - mid

    if result == target:
        return mid
    elif result > target:
        return binary(array, mid+1, end, target)
    else:
        return binary(array, start, mid-1, target)

print(binary(a, 0, max(a) , m))