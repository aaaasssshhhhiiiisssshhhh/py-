#what is percentile?
# ----> Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

import numpy 

weight = [40,45,47,48,49,50,53,70,70,80,90]

value= numpy.percentile(weight,60)

print (value)


#here the output is 53 meaning 60% of peoples have weight less or weight equal to 53