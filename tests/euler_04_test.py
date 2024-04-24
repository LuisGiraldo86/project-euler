# =================================
# Euler Project. Problem 4. Test
# =================================

# imports
from random import randrange

from project_euler.euler_04 import palindrome_three_digit_factors

# constraints
T = randrange(1, 10)
N = 10**6

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(101101, N)))

# write test cases
with open('testData/euler_04.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_04.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [palindrome_three_digit_factors(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_04.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    