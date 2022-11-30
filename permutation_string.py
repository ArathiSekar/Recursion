#Given an input string, return all permutations of the string in an array.
def permutation(str,index=0):
    
    if(index >= len(str)):
        return [""]
    
    perm = permutation(str, index + 1)
    
    result =[]
    char = str[index]
   
    for p in perm:
        
        for i in range (len(p)+1):
            result.append(p[:i] + char + p[i:])
            
    return result

str = 'abc'
print(permutation(str,0))
    
