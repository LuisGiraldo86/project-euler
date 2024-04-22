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
10<= N <= 10^12

Output Format
-------------
Print the required answer for each test case in a new line. 
"""

# solution

def largest_palindrome(N):

    triple = '{}'.format(N)[:3]
    str_pal = triple + triple[::-1]
    palindrome = int(str_pal)
    if palindrome<N:
        return palindrome, int(triple)
    else:
        triple = '{}'.format(N-1000)[:3]
        str_pal = triple + triple[::-1]
        return int(str_pal), int(triple)

def three_digit_divisors(N):

    for k in range(102,1000):
        quot, rem = divmod(N,k)
        if rem==0 and len(str(quot))==3:
            return True
    return False

def palindrome_three_digit_factors(N):

    palindrome, triple = largest_palindrome(N)

    while not three_digit_divisors(palindrome):

        triple = triple-1
        temp = '{}'.format(triple)
        pal_str = temp + temp[::-1]
        palindrome = int(pal_str)
    return palindrome
