def is_palindrome(input):
    if(len(input)<=1):
        return True

    else:
        first_char = input[0]
        last_char = input[-1]
        substring = input[1:-1]
        
        return ((first_char==last_char) and is_palindrome(substring))

if(is_palindrome("madam")):
    print("True")
else:
    print("False")
