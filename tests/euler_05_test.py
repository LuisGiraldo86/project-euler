# =================================
# Euler Project. Problem 5. Test
# =================================

# imports
from random import randrange

from project_euler.euler_05 import mcm_first_integers

# constraints
T = randrange(1, 10)
N = 40

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(101101, N)))

# write test cases
with open('testData/euler_05.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_05.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [mcm_first_integers(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_05.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    