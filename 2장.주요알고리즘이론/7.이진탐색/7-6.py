owner = int(input())
owner_list= [0]*1000001

for x in input().split():
    owner_list[int(x)] += 1

customer = int(input())
customer_list = list(map(int, input().split()))

for i in customer_list:
    if owner_list[i] > 0:
        print("yes", end=" ")
    else :
        print("no", end= " ")

