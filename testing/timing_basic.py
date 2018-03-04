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
