
#What is SciPy?
#----> SciPy is a scientific computation library that uses NumPy underneath.
#SciPy stands for Scientific Python.
#It provides more utility functions for optimization, stats and signal processing.
#Like NumPy, SciPy is open source so we can use it freely.
#SciPy was created by NumPy's creator Travis Olliphant.

#Why Use SciPy?

#-----> If SciPy uses NumPy underneath, why can we not just use NumPy?
#SciPy has optimized and added functions that are frequently used in NumPy and Data Science.



#Which Language is SciPy Written in?

#-----> SciPy is predominantly written in Python, but a few segments are written in C.



#Where is the SciPy Codebase?

#------> The source code for SciPy is located at this github repository https://github.com/scipy/scipy


#for scipy installation 
#installation by pip : python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
#installation for ubuntu and debian : sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

#mac doesnot have its own pacakge manager so we should install home brew for mac 
# installation for mac : brew install numpy scipy ipython jupyter 
#installation for fedora 22 and later : sudo dnf install numpy scipy python-matplotlib ipython python-pandas sympy python-nose atlas-devel



#
#
#mode value are those values that appears most in the list 
#
#

from scipy import stats

speed = [1,1,1,1,1,1,3,3,3,4,5,6,7,8,9,9]

x = stats.mode(speed)

print(x) 