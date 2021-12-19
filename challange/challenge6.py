#Write a Python program to check if a number is a power of a given base.


import math 

def isPower (n, base): #log10 (2)  2 = n and 10 = base
    if base == 1 and n!=1:
        return False
    
    if base ==1 and n ==1:
        return True
    
    if base ==0 and n!=1:
        return False
    
    power = int (math.log(n,base)+0.5)
    
    return base ** power ==n 

print (isPower(127,2))
print (isPower(128,2))