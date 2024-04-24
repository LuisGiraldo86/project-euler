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

from project_euler.EulerModule import eratosthenes_sieve
from math import log

# bounds for the n-th prime n log(n) and n(log(n) + log(log(n)))

class PrimeSequence:

    def __init__(self, greatest_term:int) -> None:

        self.greatest_term = greatest_term
        self.upper_bound = int(round(greatest_term*(log(greatest_term) + log(log(greatest_term))),0))
        self.sieve = eratosthenes_sieve(self.upper_bound)
        self.sequence = [k for k in range(len(self.sieve)) if self.sieve[k]]

        return None

    def nth_prime(self, N:int)->int:

        """
        Function to compute prime number sequence using Erathostones' sieve

        Parameter
        ---------
        N: int
            term of the sequence of prime numbers

        Return
        ------
        int
        """

        return self.sequence[N]
