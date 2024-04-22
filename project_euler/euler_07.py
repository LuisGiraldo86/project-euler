# =================================
# Euler Project. Problem 7
# =================================

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see that the 6th prime is 13.
What is the N^th prime number?

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10^3
1 <= N <= 10^4

Output Format
-------------
Print the required answer for each test case. 
"""

from EulerModule import eratosthenes_sieve


# bounds for the n-th prime n log(n) and n(log(n) + log(log(n)))

from math import log

n=10**4
upper_bound = n*(log(n) + log(log(n)))
upper_bound = int(round(upper_bound,0))
upper_bound



criba = eratosthenes_sieve(upper_bound)
prime_sequence = [k for k in range(len(criba)) if criba[k]]
prime_sequence[:10]

N=6
prime_sequence[N-1]
