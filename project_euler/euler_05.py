# =================================
# Euler Project. Problem 5
# =================================

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to N?

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10
1 <= N <= 40

Output Format
-------------
Print the required answer for each test case.
"""

# solution

def primes_sieve(upper_bound:int)->list:

    """
    Function to find all primes below certain upper bound using Erathostenes' sieve

    Parameters
    ----------
    upper_bound:int
        upper bound for the primes

    Return
    ------
    list of integers
    """

    primes = [2]

    lst = [k for k in range(3,upper_bound+1,2)]
    
    k=0
    while lst[k]**2<upper_bound:
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

def mcm_first_integers(N:int)->int:

    """
    Function to compute the minimum common multiple of the first N integers

    Parameter
    ---------
    N:int
        upper bound of the first consecutive integers

    Return
    ------
    int
    """

    # list of primes at most half of N
    primes = primes_sieve(N//2+1)
    
    prod = 1

    for prime in primes:
        power = 1
        while power*prime <= N:
            power = power*prime
        prod = prod*power
    return prod
        