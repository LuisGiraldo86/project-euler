# =================================
# Euler Project. Problem 8
# =================================

"""
Find the greatest product of K consecutive digits in the N digit number.

Input Format
------------
First line contains T that denotes the number of test cases. First line of each test case will contain two integers N and K. Second line of each test case will contain a N digit integer.

Constraints
-----------
1 <= T <= 100
1 <= K <= 7
1 <= N <= 1000

Output Format
-------------
Print the required answer for each test case. 
"""

# solution

def list_product(int_str:list)->int:

    """
    Computes the product of the elements of a list.

    Parameter
    ---------
    int_str: list
        list whose elements are integers but formatted as strings.

    Return
    ------
    int
    """

    int_lst = [int(num) for num in int_str]
    prod = 1

    if 0 in int_lst: return 0
    else:
        for number in int_lst:
            prod = prod*number
        return prod

def largest_product(num:int, K:int, N:int)->int:

    """
    Find the greatest product of K consecutive digits in the N digit number num.

    Parameters
    ----------
    num: int
        the number of N digits
    K: int
        number of consecutive digits
    N: int
        length of number num

    Return
    ------
    int
    """

    str_num = str(num)
    lst_num = [str_num[i:i+K] for i in range(0,N-K)]
    lst_prod = [list_product(number) for number in lst_num]
    
    return max(lst_prod)
