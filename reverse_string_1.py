def reverse_str_recursion(str):
    if(len(str) == 0):
        return ""
    elif(len(str)==1):
        return str[0]
    return reverse_str_recursion(str[1:]) + str[0]
   

str = 'happy'

print(reverse_str_recursion(str))
