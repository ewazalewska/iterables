# Create matrix using numpy.

import numpy

a= numpy.zeros((3, 3))
print(a)

""" 
[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]] 
"""

a[1][1]=1
print(a)

""" 
[[0. 0. 0.]
[0. 1. 0.]
[0. 0. 0.]] 
"""

# a[1][1]='pen' -> ValueError: could not convert string to float: 'pen'


