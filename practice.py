#Implement sum_integers(n) to calculate the sum of all integers from  1  to  𝑛  using recursion. For example, sum_integers(3) should return  6  ( 1+2+3 ).

def sum_integers(n):
    if(n==1):
        return 1
    return n+sum_integers(n-1)

print(sum_integers(3))

#Find sum of array using slicing and recursion
def sum_array(n):
    if(len(n)==1):
        return n[0]
    return n[0] + sum_array(n[1:])

n = [1,2,3,4]
print(sum_array(n))

#Find sum of array using recursion but without slicing
def sum_array_index(n,index):
    if((len(n)-1)==index):
        return n[index]
    return n[index] + sum_array_index(n, index+1)

n=[1,2,3,4]
print(sum_array_index(n,0))

#Sum of an array using iteration
def sum_array_iteration(n):
    result = 0
    for i in n:
        result += i
    return result

n =[1,2,3,4]    
print(sum_array_iteration(n))
