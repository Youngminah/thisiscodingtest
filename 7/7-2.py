n, target = map(int, input().split())
a= list(map(int,input().split()))

def binary(a,start, end, target):
    if start>end:
        return "원소가 존재하지 않습니다"
    mid = (start + end) // 2
    if a[mid] == target :
        return mid+1
    elif a[mid] < target :
        return binary(a,mid+1 ,end,target)
    else :
        return binary(a,start,mid-1,target)

print(binary(a,0, n-1, target))