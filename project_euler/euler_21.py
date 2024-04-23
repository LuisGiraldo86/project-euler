# =================================
# Euler Project. Problem 21
# =================================

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a)=b and d(b)=b, where a != b, then a and b are an amicable pair and each of a and b 
are called amicable numbers.

For example, the proper divisors of 220 are 
1, 2, 4, 5, 10, 11, 20, 22, 44, 55, and 110
therefore d(220)= 284. The proper divisors of 284 are
1, 2, 4, 71, and 142
so d(284)=220.

Evaluate the sum of all the amicable numbers under N. 

Input Format
-------------
The first line contains an integer T , i.e., number of test cases. Next T lines will contain an integer N.

Constraints
-----------
1 <= T <= 1000
1 <= N <= 10^5

Output Format
-------------
Print the values corresponding to each test case.
"""

from EulerModule import eratosthenes_sieve
import time

def sum_divisors(n):
    
    sum_div = 1
    div = 2
    while div**2 <= n:
        quot, rem = divmod(n, div)
        if rem == 0:
            sum_div += div
            if quot != div: # for perfect squares
                sum_div+=quot
        div+=1
    return sum_div

st_time = time.time()
sieve = eratosthenes_sieve(100000)

amicable_pairs = set()
divisors_sums = [1]*len(sieve)
divisors_sums[0]=0
divisors_sums[1]=0

for k in range(4, len(sieve)):
    if not sieve[k]:
        if divisors_sums[k]==1:
            divisors_sums[k]=sum_divisors(k)
        if divisors_sums[k]< len(sieve) and divisors_sums[k]>k:
            divisors_sums[divisors_sums[k]] = sum_divisors(divisors_sums[k])

        if divisors_sums[k]<len(sieve) and k != divisors_sums[k] and k == divisors_sums[divisors_sums[k]]:
            amicable_pairs.update([k, divisors_sums[k]])
        
amicable_pairs
end_time = time.time()
end_time-st_time





for k in range(4, len(sieve)):
    if not sieve[k]:
        d1 = sum_divisors(k)
        if d1< len(sieve) and k == sum_divisors(d1) and k != d1:
            amicable_pairs.update([k,d1])

amicable_pairs




def sum_proper_divisors(N):

    sum_div = [0]*(N+1)
    for k in range(2, N+1):
        sum_div[k] = sum_divisors(k)
    return sum_div
    
def amicable_pairs(N):

    amicable = []
    sum_divisors = sum_proper_divisors(N)
    upper = len(sum_divisors)
    for k in range(4, upper):
        if sum_divisors[k]<upper and sum_divisors[k] != k:
            d1 = sum_divisors[k]
            if sum_divisors[d1] == k:
                amicable.append([k,d1])
            
    return amicable




test = sum_proper_divisors(300)
test

amicable_pairs(5000000)
