# =================================
# Euler Project. Problem 23
# =================================

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Given N, print YES if it can be expressed as sum of two abundant numbers, else print NO.

Input Format
-------------
The first line contains an integer T , i.e., number of test cases. Next T lines will contain an integer N.

Constraints
-----------
1 <= T <= 100
1 <= N <= 10^5

Output Format
-------------
Print the values corresponding to each test case.
"""

from EulerModule import sum_proper_divisors

upper = 10**5

abundant_num = [True if sum_proper_divisors(k)>k else False for k in range(0,upper) ]

def abund_sum(n, abund_lst):

    for k in range(12, n//2+1):
        if abund_lst[k] and abund_lst[n-k]:
            return 'YES'
    return 'NO' 
