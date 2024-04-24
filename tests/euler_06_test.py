# =================================
# Euler Project. Problem 6. Test
# =================================

# imports
from random import randrange

from project_euler.euler_06 import sum_squares_difference

# constraints
T = randrange(1, 10**4)
N = 10**4

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(1, N)))

# write test cases
with open('testData/euler_06.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_06.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [sum_squares_difference(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_06.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    