#Reverse string using recursion
def reverse_string(input):
    if(len(input)==0):
       return ""
    else:
        first_char = input[0]
        rest_string = slice(1,None)
        substring = input[rest_string]
        
        
        #print(first_char)
        #print(substring)
        r = reverse_string(substring)
        return (r+first_char)
        

if(reverse_string("abc")=="cba"):
    print("Pass")
