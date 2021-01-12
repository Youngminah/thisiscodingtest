n, target = map(int, input().split())
a= list(map(int,input().split()))

def binary(start, end, target, a):

    while( start <= end) :
        mid = (start + end) // 2
        if(a[mid] == target):
            return mid + 1
        elif(a[mid] > target) :
            end = mid -1
        else:
            start = mid+1
    return "원소가 존재하지 않습니다"

print(binary(0, n-1, target,a))
