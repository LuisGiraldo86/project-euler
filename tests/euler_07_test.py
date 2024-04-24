# =================================
# Euler Project. Problem 7. Test
# =================================

# imports
from random import randrange

from project_euler.euler_07 import PrimeSequence

# constraints
T = randrange(1, 10**4)
N = 10**4

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(1, N)))

primes = PrimeSequence(N)

# write test cases
with open('testData/euler_07.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_07.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [primes.sequence[int(n[:-1])-1] for n in tests[1:]]

with open('solutions/euler_07.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    