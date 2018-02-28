"""

Determine if a given year is a leapyear

In the Gregorian calendar three criteria must be taken into account to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

Template:            
def is_leap(year):
    leap = False
    
    # Write your logic here
    return leap

"""

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4 == 0:
        if year%400 ==0:
            leap = True
        elif year%100 ==0:
            leap = False
        else:
            leap = True
    return leap
