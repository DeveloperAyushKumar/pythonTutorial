def sum (a,b):
    return a+b
print(sum(4,4))
def avg(a,b,c):
    return (a+b+3)/3
print(avg(3,4,3))

def cal_prod(a=1,b=1):
    return a*b
print(cal_prod())

def f(a,b=1):
    return a+b

# WAF to print length of a list
def listLen(a):
    print(len(a))

# WAF to print the length of a list in a single line 
def printList(a):
    for ele in a:
        print(ele, end=" ")
# WAF to find the factorial of n 
def fac (a):
    if(a==0): 
        return 1
    return fac(a-1)*a

