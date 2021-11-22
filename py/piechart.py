import matplotlib.pyplot as pyplot
import numpy as np 

data =np.array ([50,20,10,15,5])
labels =['python', 'js', 'c', 'java' ,'php']

pyplot.pie (data , labels = labels ,shadow =True)
pyplot.show()



# for this code to work you need 
# pip
#2 matplotlib : python -m pip install -U matplotlib ( it has functions that help matplotlib to work as matlab)
#3 numpy : python3 -m pip install -U numpy  