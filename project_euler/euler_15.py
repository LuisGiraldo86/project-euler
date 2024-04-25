# =================================
# Euler Project. Problem 15
# =================================

"""
Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a NxM grid? As number of ways can be very large, print it modulo (10^9+7).

Input format
------------
The first line contains an integer T i.e. the number of test cases. 

Next T lines will contain integers N and M.

Constraints
-----------

1 <= T <= 10^3
1 <= N <= 500
1 <= M <= 500

Output format
-------------
Print the values corresponding to each test case.
"""

# solution

from math import factorial as F

def counting_path(N:int, M:int)->int:

    comb = F(N+M)//(F(N)*F(M))

    return comb%(10**9+7)
