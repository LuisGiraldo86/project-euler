# =================================
# Euler Project. Problem 1. Test
# =================================

# imports

from random import randrange

from project_euler.euler_01 import euler_project_1

# constraints
T = randrange(1, 10**5)
N = 10**9

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(1, N)))

# write test cases
with open('testData/euler_01.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_01.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [euler_project_1(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_01.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    