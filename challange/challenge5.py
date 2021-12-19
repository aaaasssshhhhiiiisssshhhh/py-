# Write a Python program to check if an integer is the power of another integer

def isPower(x,y):
    while (x%y ==0):
        x =x/y
    return x ==1
print (isPower(16,2))    