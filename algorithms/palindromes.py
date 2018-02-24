"""
What is the only (double-digit, or above) Prime number that is
palindromic in both base-2 (binary), and base-10 (decimal) instances?
"""

import math

def to_binary(n):
    return(bin(n)[2:])
    
#print(to_binary(6))

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

#def generate_decimal_palindromes(limit):

def isPalindrome(n):
    n=str(n)
    palindrome=True
    for i in range(len(n)//2):
        if n[i] != n[-i-1]:
            palindrome=False
            break
    return palindrome

#print(isPalindrome(22322))
    

i=10
while True:
    i += 1
    if isPrime(i):
        if isPalindrome(i):
            if isPalindrome(to_binary(i)):
                print(i)
                break
