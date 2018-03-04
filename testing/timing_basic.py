"""

A basic resource for measuring the time-performance of code using the timeit module

To use timeit you create a Timer object whose parameters are two Python statements. 
The first parameter is a Python statement that you want to time; 
the second parameter is a statement that will run once to set up the test. 
The timeit module will then time how long it takes to execute the statement some number of times. 

By default timeit will try to run the statement one million times. 
When its done it returns the time as a floating point value representing the total number of seconds. 

"""

from timeit import Timer


# Simple timeing
# Define a function to be timed
def test1():
    l = []
    for i in range(1000):
        l = l + [i]
        
# Declare a timer
# Note: "from __main__ import test1" ... this imports the test into a new timer namespace so that no variables interfere
# and to try to ensure a clean testing space.
# Also Note: you can declare the timer before declaring the function
t1 = Timer("test1()", "from __main__ import test1")

# Run the Timer
print("concat ",t1.timeit(number=1000), "milliseconds")




# Timing comparison of Dictionary operations
import random
for i in range(10000,1000001,20000):
    tget = timeit.Timer("x.get(random.randrange(%i),0)"%i,
                     "from __main__ import random,x")
    tset = timeit.Timer("x[random.randrange(%i)] = %i"%(i,i),
                     "from __main__ import random,x")
    x = {j:j for j in range(i)}
    get_time = tget.timeit(number=1000)
    set_time = tset.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, get_time, set_time))
