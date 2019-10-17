# This takes various items of a list and converts
# them to numbers and then the total
total = 0
import numpy as np
s = [1.23, 2.4, 3.123] # This a list
list_int = np.array(s) # This is a numpy integer array
print list_int # just to check the list
x = len(list_int)
print x     # just to check the items counted
print sum(list_int) # another command to sum

for j in range(x):  # using for loop for summation instead
# of sum command
    total = total + list_int[j]
print total
    
