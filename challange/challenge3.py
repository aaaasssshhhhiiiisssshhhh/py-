# Write a Python program to check if a given positive integer is a power of four

def powee3 (n):
    while (n%3 ==0):
        n /=3
    return n ==1
    
print (powee3(27))