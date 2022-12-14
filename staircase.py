#Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has n steps?
#Write a recursive function to solve the problem.
#Example:
#n == 1 then answer = 1
#n == 3 then answer = 4

def staircase(n):
    if (n==1):
        return 1
    elif (n < 1):
        return None
    elif (n==2):
        return 2
    elif (n == 3):
        return 4
    else:
        return (staircase(n-1) + staircase(n-2)+ staircase(n-3))

n = 7
print(staircase(n))
