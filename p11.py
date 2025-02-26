#calculator
# if(c=="+"):
def add(a,b):
    return a+b
#     print(add(a,b))

# elif(c=="-"):
def sub(a,b):
    return a-b
#     print(sub(a,b))

# elif(c=="*"):
def mul(a,b):
    return a*b
#     print(mul(a,b))

# elif(c=="//"):
def div(a,b):
    return a//b
#     print(div(a,b))

# elif(c=="%"):

def rem(a,b):
    return a%b
#     print(rem(a,b))

# elif(c=="^"):

def pow(a,b):
    return a**b
#     print(pow(a,b))

a=float(input("enter the 1st number"))
b=float(input("enter the 2nd number"))
c=str(input("enter the operation"))

if c.lower() =="add":
    r=add(a,b)
    print(r)

elif c.lower() =="sub":
    r=sub(a,b)
    print(r)

elif c.lower() =="div":
    r=div(a,b)
    print(r)

elif c.lower() =="mul":
    r=mul(a,b)
    print(r)

elif c.lower() =="rem":
    r=rem(a,b)
    print(r)

elif c.lower() =="pow":
    r=pow(a,b)
    print(r)












 