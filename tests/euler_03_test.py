# =================================
# Euler Project. Problem 3. Test
# =================================

# imports
from random import randrange

from project_euler.euler_03 import largest_prime_factor

# constraints
T = randrange(1, 10)
N = 10**12

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(10, N)))

# write test cases
with open('testData/euler_03.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_03.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [largest_prime_factor(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_03.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    