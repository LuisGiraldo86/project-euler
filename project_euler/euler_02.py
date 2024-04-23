# =================================
# Euler Project. Problem 2
# =================================

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10^5
10<= N <= 4*10^16

Output Format
-------------
Print the required answer for each test case. 
"""

# solution

def even_fibonacci_sum(upper_bound:int)->int:

    """
    Function to compute the sum of the even elements of Fibonacci sequence not exceding upper_bound.

    Parameter
    ---------
    upper_bound: int
        upper bound for the elements of Fibonacci sequence.

    Return
    ------
    int
    """

    result = 0
    fibonacci = [1,1]

    while fibonacci[1] < upper_bound:

        if fibonacci[1]%2 == 0:
            result += fibonacci[1]
        temp = fibonacci[1]
        fibonacci[1] = fibonacci[1] + fibonacci[0]
        fibonacci[0] = temp
    return result
