import math
import random
from sympy import *
from sympy.ntheory import discrete_log


# Function to calculate x for given a, b, m: a^x = b mod m
def discreteLogarithm(a, b, m):
    return discrete_log(m, b, a)


# generate a prime number in range (a,b)
def prime_generator(a, b):
    check = true
    while check:
        i = random.randrange(a, b)
        if isprime(i):
            check = false
    return i


# find a prime divisor of p -1
def divisor_number(p):
    for q in range(pow(2, 10), (p - 1) // 2):
        if (p - 1) % q == 0 & isprime(q):
            return q


# Utility function to store prime
# factors of a number
def findPrimefactors(s, n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        s.add(2)
        n = n // 2

    # n must be odd at this point. So we can skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):

        # While i divides n, print i and divide n
        while n % i == 0:
            s.add(i)
            n = n // i

    # This condition is to handle the case
    # when n is a prime number greater than 2
    if n > 2:
        s.add(n)


# Function to find the smallest primitive
# root of n
def findPrimitive(n):
    s = set()

    # Check if n is prime or not
    if not isprime(n):
        return -1

    # Find value of Euler Totient functionof n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:
            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if pow(r, phi // it, n) == 1:
                flag = True
                break

        # If there was no power with value 1.
        if not flag:
            return r
    # If no primitive root found
    return -1
