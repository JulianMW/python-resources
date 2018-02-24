
# Problem: return the sum of all even fibonacci numbers up to 4 million
# Solution: recursively generate the next number in the sequence and add if it is even

def nextnum(a,b):
    next_fib = a+b
    if next_fib > 4000000:
        return 0
    elif next_fib%2 ==0:
        return next_fib + nextnum(b,next_fib)
    else:
        return nextnum(b,next_fib)

print(nextnum(1,1))
