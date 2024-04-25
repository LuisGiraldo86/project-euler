# =================================
# Euler Project. Problem 9. Test
# =================================

# imports
from random import randrange

from project_euler.euler_09 import triples_conditioned

# constraints
T = randrange(1, 3000)
N = 3000

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(1, N)))

# write test cases
with open('testData/euler_09.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_09.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [triples_conditioned(int(n[:-1])-1) for n in tests[1:]]

with open('solutions/euler_09.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    