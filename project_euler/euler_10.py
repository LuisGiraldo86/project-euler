# =================================
# Euler Project. Problem 10
# =================================

"""
The sum of the primes below 10 is 2+3+5+7=17.

Find the sum of all the primes not greater than given N.

Input Format

The first line contains an integer T i.e. number of the test cases.
The next T lines will contains an integer N.

Constraints
-----------
1 <= T <= 10^4
1 <= N <= 10^6

Output Format
-------------
Print the value corresponding to each test case in separate line.
"""

# solution

from EulerModule import eratosthenes_sieve


ind_primes = eratosthenes_sieve(1000000)
sumation=[0]*len(ind_primes)

for k in range(1,len(ind_primes)):
    sumation[k]+=sumation[k-1] + k*ind_primes[k]
