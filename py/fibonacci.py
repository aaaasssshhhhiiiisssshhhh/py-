#fibonacci is series which continue as pattern : 0 1 1 2 3 5 8 13 ........
#here first two numbers are add and palced in on going series 
# for example a=0 ; b = 1 then c = 0+1 = 1 so the series be like : 0 1 1 
#now first value a=1 and second value b =1 so c = 1+1=2
#again first value a= 1 and second value b = 2 so c= 1+2 =3
#like wise the series continues up to the number you like.


#lets code in this idea 😛

def fibo(n): # here we define fibonacci series upto n 
    print("displaying series upto n")

    a=0 # lets take initial value as 0
    b=1 #lets take our second value as 1 like in series first two terms 
    
    while a < n: #this while loop continue if value of a <n
        print (a,end='')
        a,b = b, a+b
        print()
fibo(2000)        