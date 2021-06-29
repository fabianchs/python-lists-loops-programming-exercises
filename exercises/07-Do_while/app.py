
#Your code go here:

x=20

while x>=0:
    if x%5==0 and x!=0:
        print(str(x)+"!")
    elif x%5!=0:
        print(x)
    
    if x==0:
        print("LIFTOFF")
    x=x-1