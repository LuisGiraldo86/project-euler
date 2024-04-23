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

def sum_arith_prog(a_0:int, n:int, d:int)->int:

    """
    Computes the sum of an arithmetic progression.

    Parameters
    ----------
    a0: int
        First term of the arithmetic progression
    n: int
        Number of terms from the progression to be added
    d: int
        difference between the terms of the arithmetic progression 
    
    Return
    ------
    int
    """

    result = n*(a_0 + a_0 + (n-1)*d)//2
    
    return result

def find_last_term(upper_bound:int, number:int)->int:

    """
    Computes how many times can a number be added without surpasing an upper bound

    Parameters:
    -----------
    upper_bound: int
        upper bound for the number of times that we add number to itself
    number: int
        number to add to itself
    
    Returns
    -------
    int
    """
    
    if upper_bound%number == 0:
        return upper_bound//number-1
    else:
        return upper_bound//number

# solution

def euler_project_1(N:int)->int:

    """
    Compute the sum of all multiples of 3 or 5 below N

    Parameter
    ---------
    N: int
        upper bound for the multiples of 3 or 5 considered

    Returns
    -------
    int 
    """

    n_3 = find_last_term(upper_bound=N, number=3)
    mult_3 = sum_arith_prog(a_0=3, n=n_3, d=3)

    n_5 = find_last_term(upper_bound=N, number=5)
    mult_5 = sum_arith_prog(a_0=5, n=n_5, d=5)
    
    n_15 = find_last_term(upper_bound=N, number=15)
    mult_15 = sum_arith_prog(a_0=15, n=n_15, d=15)

    return mult_3 + mult_5 - mult_15
