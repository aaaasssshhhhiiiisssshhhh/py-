#what is histogram??
#----> To visualize the data set we collected we draw a histogram..
#in python we use matplotlib to draw histogram

#what is matplotlib?
#----> it is a low level graph plotting library in pyhthon that serve as 
#visualization utility.
#it was created by John D. hunter 
#it is a open source library and can be use freely.
#Matplotlib is written in python and few segements are written in c, 
#objective-C and Javascript for platform comaptibility.

#lets code..

import numpy 
import matplotlib.pyplot as aashish #Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:


x = numpy.random.uniform (0.0, 3.0,10)

aashish.hist(x,10)
aashish.show()