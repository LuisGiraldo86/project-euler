# =================================
# Euler Project. Problem 5
# =================================

"""
2520 is the smallest number that can be divided by each of the numbers from to without any remainder.
What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from 1 to N?

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10
1 <= T <= 40

Output Format
-------------
Print the required answer for each test case.
"""

# solution

def sieve(N):

    primes = [2]

    lst = [k for k in range(3,N+1,2)]
    
    k=0
    while lst[k]**2<N:
        prime = lst[k]
        for i in range(k+1,len(lst)):
            if prime==0:
                continue
            elif lst[i]%prime == 0:
                lst[i]=0
        k+=1
        
    for prime in lst:
        if prime != 0:
            primes.append(prime)
    return primes

def mcm(N):

    primes = sieve(20)
    prod = 1

    for prime in primes:
        power = 1
        while power*prime <= N:
            power = power*prime
        prod = prod*power
    return prod
        