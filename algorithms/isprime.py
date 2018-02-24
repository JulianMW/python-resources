import math
def isPrime(n):
	i=1
	prime=True
	while True:
	   i+=1
	   if n%i ==0:
	       prime = False
	       break
	   if i>math.sqrt(n):
	       break
	return prime
	       
	
# Tests....
print isPrime(3) # Should output True
print isPrime(143) # Should output False
print isPrime(790003) # Should output True
