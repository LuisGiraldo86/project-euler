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

def list_product(int_str):

    int_lst = [int(num) for num in int_str]
    prod = 1
    for number in int_lst:
        if number == 0:
            return 0
        else:
            prod = prod*number
    return prod

def largest_product(num, K, N):

    str_num = str(num)
    lst_num = [str_num[i:i+K] for i in range(0,N-K)]
    lst_prod = [list_product(number) for number in lst_num]
    return max(lst_prod)
