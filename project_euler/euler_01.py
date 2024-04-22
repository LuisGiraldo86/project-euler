# =================================
# Euler Project. Problem 1
# =================================

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10^5
1 <= N <= 10^9
Output Format
-------------
For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.
"""

# auxiliary functions

def sum_arith_prog(n:int, d:int)->int:
    
    return ((n+1)*(2*0 + n*d))//2

def find_n(d:int, N:int)->int:
    
    if N%d == 0:
        return N//d-1
    else:
        return N//d

# solution

def euler_project_1(N)->int:

    n_3 = find_n(d=3, N=10)
    mult_3 = sum_arith_prog(n=n_3, d=3)

    n_5 = find_n(d=5, N=10)
    mult_5 = sum_arith_prog(n=n_5, d=5)
    
    n_15 = find_n(d=15, N=10)
    mult_15 = sum_arith_prog(n=n_15, d=15)

    return mult_3 + mult_5 - mult_15
