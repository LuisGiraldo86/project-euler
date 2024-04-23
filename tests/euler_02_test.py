# =================================
# Euler Project. Problem 2. Test
# =================================

# imports

from random import randrange

from project_euler.euler_02 import even_fibonacci_sum

# constraints
T = randrange(1, 10**5)
N = 4*(10**16)

# test values
lines = [str(T)]
for k in range(T):
    lines.append(str(randrange(1, N)))

# write test cases
with open('testData/euler_02.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_02.txt', 'r') as file:
    tests = file.readlines()

# compute solutions
solutions = [even_fibonacci_sum(int(n[:-1])) for n in tests[1:]]

with open('solutions/euler_02.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    