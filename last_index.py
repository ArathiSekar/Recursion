#Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.
#For example:
#For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 5, output = 6
#For arr = [1, 2, 5, 5, 1, 2, 5, 4] and target = 7, output = -1

def last_index(arr,target):
    index_last = -1
    for i in range(0,len(arr)):
        if (arr[i] == target):
            index_last = i
    
    return index_last
            

def last_index_recursion(arr,target,index_last):
    if(index_last < 0):
        return -1
    elif (arr[index_last] == target):
        return index_last
    else:
        return last_index_recursion(arr, target, index_last-1 )
    
    

arr = [1, 2, 5, 5, 1, 2, 5, 4]
target = 6
print(last_index(arr,target))
print(last_index_recursion(arr,target,len(arr)-1))
