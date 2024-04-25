# =================================
# Euler Project. Problem 9
# =================================

"""
A Pythagorean triplet is a set of three natural numbers, a<b<c, for which, 
   a^2+b^2=c^2.
For example, 3^2+4^2=5^2.

Given N, check if there exists any Pythagorean triplet for which a+b+c=N. Find maximum possible value of abc among all such Pythagorean triplets. If there is no such Pythagorean triplet print -1.

Input Format
------------
The first line contains an integer T, i.e. number of test cases. The next lines will contain an integer N.

Constraints
-----------
1 <= T <= 3000
1 <= N <= 3000

Output Format
-------------
Print the value corresponding to each test case in separate lines.
"""

def triples_conditioned(N:int)->int:

    """
    Function to determine existence of a Pythagorean triplet a, b, c such that a+b+c=N. If it exists, find the maximum value of the product a*b*c among all those triplets.

    Parameter
    ---------
    N: int
        value of the sum of the Pythgorean triplet

    Return
    ------
    int
    """

    N_squared = N**2
    if N<12 or N%2==1: # (3,4,5) is the first Pythagorean triplet, the sum of a triplet is always even
        return -1
    else:
        max_prod=1
        for a in range(1,N//3):
            quot, rem = divmod(N_squared-2*a*N, 2*(N-a))
            if rem == 0:
                max_prod = max(max_prod, a*quot*(N-a-quot))
    
    if max_prod>1:return max_prod
    else: return -1
