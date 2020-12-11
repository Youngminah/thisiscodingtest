owner = int(input())
owner_list= list(map(int, input().split()))

customer = int(input())
customer_list = list(map(int, input().split()))

def binary(target, array, start, end):
    if(start>end):
        return "no"
    mid = (start+end)//2
    if owner_list[mid] == target :
        return "yes"
    elif owner_list[mid]> target:
        return binary(target,array,start,mid-1)
    else:
        return binary(target,array,mid+1,end)

for x in customer_list:
    print(binary(x,owner_list,0,len(owner_list)-1), end=" ")