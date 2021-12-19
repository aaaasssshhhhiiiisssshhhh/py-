#Write a Python program to check if a given positive integer is a power of three.

'''

a = int (input ('enter max number'))
if a % 2 ==0:
    print('true')
else:
    print("flase")

'''

#other method :


def powerOf2 (n):
    return n > 0 and (n & (n-1) == 0) # if n =n then tha value should be 1.. since n is not = (n-1 ) thats why n==0
print (powerOf2 (4))    




