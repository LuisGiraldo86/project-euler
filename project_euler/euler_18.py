# =================================
# Euler Project. Problem 18
# =================================

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23. The path is denoted by numbers in bold.

     *3*
   *7*  4
  2  *4*   6
 8  5  *9*  3

 That is 3+7+4+9=23.

 Find the maximum total from top to bottom of the triangle given in input.

Input Format
------------

First line contains T, the number of testcases. For each testcase:
First line contains N, the number of rows in the triangle.
For next N lines, i'th line contains i numbers.

Constraints
-----------
1 <= T <= 10
1 <= N <= 15
0 <= numbers <= 100

Output Format
-------------
For each test case, print the required answer in a new line.
"""

def new_triangle(old_tri:list, pos:int)->list:

    """
    Function to build a new triangle from the elements of the second line.

    Parameters
    ----------
    old_tri: list of lists
        original triangle to extract the new one.
    pos: int
        if its value is 0 the top element is the one in old_tri[1][0], if it is 1 the top element of the new triangle is old_tri[1][1].

    Return
    ------
    list of lists
    """

    if pos==0:
        new_tri = [lst[0:-1] for lst in old_tri[1:]]
    if pos==1:
        new_tri = [lst[1:] for lst in old_tri[1:]]

    return new_tri

def total_paths(triangle):

    """
    Function to construct all possible paths from top to bottom of the triangle.

    Parameter
    ---------
    triangle: list of lists
        list of list containing the values of the triangle.

    Returns
    -------
    list of lists
    """

    paths = [[(0,0)]]
    for k in range(1,len(triangle)):
        temp = []
        for n in range(len(triangle[k])):
            for path in paths:
                if path[-1]==(k-1,n-1) or path[-1]==(k-1,n):
                    temp.append(path + [(k,n)])
        if len(temp)!=0:
            paths = temp
    return paths

def max_path(triangle:list)->int:

    """
    Function to find the value of the maximum path exploring all possible values.

    Parameters
    triangle: list
        list of lists containing the values conforming the triangle

    Return
    ------
    int 
    """

    all_paths = total_paths(triangle)
    maximum = 0
    for path in all_paths:
        partial_maximum = 0
        for pos in path:
            partial_maximum += triangle[pos[0]][pos[1]]
        maximum = max(maximum, partial_maximum)
    return maximum
