# -*- coding: utf-8 -*-
#Experimental
def sum(x,y):
    z= x+y
    return(z)

sum(1,2)
sum(3,4)

def prime(x):
    if x==2:
        return(True)
    elif x==3:
        return(True)
    for i in range(2,x-1):
        out= x % i
        if out==0:
            return(False)
    return(True)    

prime(7)
