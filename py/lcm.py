x = int (input(' enter first number:'))
y = int (input ('enter second number:'))
if (x>y):
    number =x
else:
    number =y 
while (True):
    if (number % x ==0 and number % y ==0):
        print("the lcm is ",number)
        break;
    number = number +1                       
    
    
    
    
    