# =================================
# Euler Project. Problem 14
# =================================

"""
The following iterative sequence is defined for the set of positive integers:

n --> n/2, n is even
n --> 3*n+1, n is odd. 

Using the rule above and starting with 13, we generate the following sequence:
 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, <=N produces the longest chain? If many possible such numbers are there print the maximum one.

Note: Once the chain starts the terms are allowed to go above N.

Input Format
------------
The first line contains an integer T, i.e., number of test cases. Next T lines will contain an integer N.

Constraints
-----------
1 <= T <= 10^4
1 <= N <= 10^6

Output Format
-------------
Print the values corresponding to each test case.
"""

# solution

def length_collatz_seq(N, stop):
    
    count = 0
    while N >1 and N>stop:
        quot, rem = divmod(N,2)
        if rem==0:
            N=quot
            count+=1
        else: 
            N=(3*N+1)//2
            count+=2
    return count, N

def collatz_lengths(N):

    lst = [0,1]
    for k in range(2, N+1):
        if k%2==0:
            lst.append(lst[k//2]+1)
        else: 
            length, n = length_collatz_seq(k, k-1)
            lst.append(length+lst[n])
    return lst

def max_lengths(N):

    collatz_len = collatz_lengths(N)
    lst_n = [0]
    max_length = 1
    for k in range(1, len(collatz_len)):
        if collatz_len[k]==max_length: lst_n.append(k)
        elif collatz_len[k]>max_length: 
            lst_n.append(k)
            max_length = collatz_len[k]
        else: continue
    return lst_n
