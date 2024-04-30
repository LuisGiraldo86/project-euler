# =================================
# Euler Project. Problem 13
# =================================

"""
Work out the first ten digits of the sum of N 50-digit numbers.

Input Format
------------
First line contains N, next N lines contain a 50 digit number each.

Constraints
-----------
1 <= N <= 10^3

Output Format
-------------
Print only first 10 digit of the final sum 
"""

# solution
def first_ten(lst:list)->str:

    """
    Function to sum all the elements of a list with 50 digits numbers

    Parameter
    ---------
    lst: list
        list with integers with 50 digits

    Return
    ------
    str
    """

    total_sum = sum(lst)
    return str(total_sum[10:])
