"""
A Pythagorean triplet is a set of three natural numbers, a b c, for which,
a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find it
"""

for x in range(1,1000):
    for b in range (1,1000-x):
        if (x**2 + b**2) == ((1000-x-b)**2):
            #if a+b+
            print(x,b,(1000-x-b))
            break
    if (x**2 + b**2) == ((1000-x-b)**2):
        break
a=x*b*(1000-x-b)
print(a)
