#what is standard deviation ?
# --> Standard deviation is a number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.


# here we use numpy std() method 

#Standard Deviation is often represented by the symbol Sigma: σ

import numpy

x = [100,200,300,400] #take any values in array

#here we calcutate sd 
SD = numpy.std(x) 

print (SD)

