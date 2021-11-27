#what is dataset?
#----> A data set is a collection of data. In the case of tabular data, a data set corresponds to one or more database tables,
# where every column of a table represents a particular variable, and each row corresponds to a given record of the data set in question

#how can we create  big dataset?
#-----> To create big data sets for testing, we use the Python module NumPy,
# which comes with a number of methods to create random data sets, of any size.


#what is  data distribution?
# ----> In the real world, the data sets are much bigger, 
# but it can be difficult to gather real world data, at least at an early stage of a project.


import numpy

values = numpy.random.uniform (0.0, 5.0, 10) #here we create 10 random floating point number form 0 to 5.

print ("10 random floating point number from 0 to 5 are=", values)


#output = 10 random floating point number from 0 to 10 are= [4.34873642 1.62014346 0.62717136 3.617578   3.91833963 4.45850834 3.88071574 0.49087419 0.60267731 1.70242934]