# =================================
# Euler Project. Problem 6
# =================================

"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ··· + 10^2 = 385. The square of the sum of the first ten natural numbers is, (1 + 2 + ··· + 10)^2 = 3025. Hence the absolute difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum.

Input Format
------------
First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
-----------
1 <= T <= 10^4
1 <= N <= 10^4

Output Format
-------------
Print the required answer for each test case. 
"""

# solution

def sum_squares_difference(N):

    squared_sum = ((N*(N+1))//2)**2

    sum_squares = (N*(N+1)*(2*N+1))//6
    
    return abs(sum_squares-squared_sum)
