#Write a Python program to check if a given positive integer is a power of two



# '''
# Do you want to assign one or more elements of a list specifically and assign all the remains to something else? Easy with Python.

# Check out this syntax that makes use of * unpacking notation in Python:
# '''

# list = [5, 10, 20, 30]
# x , y, *z =list
# print(x)
# print(y)
# print(z)

# '''
# output:

# 5
# 10
# [20, 30]


# '''


# list = ['ram', 'hari','gita' , 'shita', 'rakhxya' ]

# a,b,*c,b =list
# print (a)
# print (b)
# print (c)
# '''
# aaba output ma b ma ta hari thiyo but aaba rakhxya replace hari 
# last ma feri b call garera 

# '''


list = ['ram', 'hari','gita' , 'shita', 'rakhxya' ]

a,b,b,*c =list #b feri call garda hari ko thau ma aaba git basyo beacuse 3rd character 
print (a)
print (b)
print (c)