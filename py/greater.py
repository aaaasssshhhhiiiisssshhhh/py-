#lets have some fun trying new ways to compare two number 

#how do you compare greater of two numbers ?? ğ¤

x = int ( input ('enter first number:'))
y = int ( input ('enter second number:'))


if x>y:
    print ('the greater number is x:',+x)

else:
    print( 'the greater number is y:',+y)    
    
    
    
#we can compare this by following way as well 
# we can use iğ

result = x if x > y else y
print ( 'the greater number is :', result)