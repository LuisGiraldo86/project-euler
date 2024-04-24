# =================================
# Euler Project. Problem 3
# =================================

"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of a given number N?

Input Format
------------
First line contains T, the number of test cases. This is followed by T lines each containing an integer N.

Constraints
-----------
1 <= T <= 10
10<= N <= 10^12

Output Format
-------------
For each test case, display the largest prime factor of N. 
"""
# solution

def largest_prime_factor(N:int)->int:

    """
    Compute the largest prime divisor of a postive integer N

    Parameter
    ---------
    N: int
        positive integer value

    Return
    ------
    int
    """

    while N%2==0: N//= 2  # Remove all even factors

    divisor = 3
    while divisor**2 <= N:
        if N%divisor == 0:
            N = N//divisor
        else:
            divisor += 2
    if N==1:
        return 2
    else:
        return N
