# =================================
# Euler Project. Problem 20
# =================================

"""
n! means n*(n-1)*(n-2)*···*3*2*1

For example,
10! = 10*9*8*7*6*5*4*3*2*1 = 3628800,
and the sum of the digits in the number 10! is  3+6+2+8+8=27.

Find the sum of the digits in the number N!.

Input Format
-------------
The first line contains an integer T , i.e., number of test cases. Next T lines will contain an integer N.
"""

from math import factorial as f

N=2
M=3

f(N+M)//(f(N)*f(M))%(10**9+7)
