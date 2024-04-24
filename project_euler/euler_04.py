# =================================
# Euler Project. Problem 4
# =================================

"""
A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 
101101 = 143*707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than N.

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10
101101 < N < 10^12

Output Format
-------------
Print the required answer for each test case in a new line. 
"""

# solution
def largest_palindrome(upper_bound:int)->tuple:

    """
    Function to find the greatest six-digit palindrome below certain upper bound.

    Parameter
    ---------
    upper_bound: int
        upper bound of the six-digit palindrome

    Return
    ------
    int
    """

    triple = str(upper_bound)[:3]
    str_pal = triple + triple[::-1]
    palindrome = int(str_pal)

    if palindrome<upper_bound:
        return palindrome, int(triple)
    else:
        triple = str(upper_bound-1000)[:3]
        str_pal = triple + triple[::-1]
        return int(str_pal), int(triple)

def three_digit_divisors(N:int)->bool:

    """
    Function that determines if certain integer N has a three digit divisor.

    Parameter
    ---------
    N: int
        integer to determine if it has a three digit divisor

    Return
    ------
    bool
    """

    for k in range(100,1000):
        if k**2 < N:
            quot, rem = divmod(N,k)
            if rem==0 and len(str(quot))==3:
                return True
        else:
            continue
    return False

def palindrome_three_digit_factors(upper_bound:int)->int:

    """
    Function to determine the largest six-digit palindrome below certain upper bound and it is the product of two three-digit numbers.

    Parameter
    ---------
    upper_bound: int
        upper bound for the six digit palindrome

    Return
    ------
    int
    """

    palindrome, triple = largest_palindrome(upper_bound)

    while not three_digit_divisors(palindrome):

        triple = triple-1
        temp = str(triple)
        pal_str = temp + temp[::-1]
        palindrome = int(pal_str)
    return palindrome
