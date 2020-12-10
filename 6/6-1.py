array = [ 7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    value = i
    for j in range(i+1, len(array)):
        if array[value] > array[j] :
            value = j
    array[value] , array[i] = array[i] , array[value]


print(array)
