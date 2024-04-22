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
# auxiliary functions

import time


def largest_prime_factor(N:int)->int:

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


def execution_time(function, N, reps):
    total_time = 0
    count = 0
    for k in range(0,reps):
        str_time = time.time()
        function(N)
        end_time = time.time()
        ex_time = end_time - str_time
        total_time = total_time + ex_time
        count=count+1
    return total_time/reps, count


time1, count = execution_time(largest_prime_factor, 600851475143, 1000)
time1
