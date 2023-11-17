# write a function to add numbers with return type
# function with arg and return type

def add(*a):
    s=0
    for i in a:
        s+=i
    return(s)
# print(add(1,2,3))

# rev_string
def rev(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return(rev)
# print(rev(123))



# armstrong
def arm(n):
    samp=n
    arms=0
    while n!=0:
        rem=n%10
        arms+=rem**3
        n//=10
    if samp==arms:
        return('armstrong')
    else:
        return('not armstrong')
# print(arm(153))
# print(arm(125))



