# =================================
# Euler Project. Problem 16
# =================================

"""
 2^9=512 and the sum of its digits is 5+1+2=8.

What is the sum of the digits of the number 2^N?

Input Format
------------
The first line contains an integer T, i.e., number of test cases. Next T lines will contain an integer N.

Constraints
-----------
1 <= T <= 100
1 <= N <= 10^4

Output Format
-------------
Print the values corresponding to each test case.
"""

n=9

str_power2 = str(2**n)
digits = [int(digit) for digit in str_power2]
result = sum(digits)
result
