# =================================
# Euler Project. Problem 8. Test
# =================================

# imports
from random import randrange

from project_euler.euler_08 import largest_product

# constraints
T = randrange(1, 10)

# test values
lines = [str(T)]
for k in range(T):
    K = randrange(1,7)
    N = randrange(K, 10)
    num = randrange(10**(N-1), 10**(N)-1)
    lines.append(str(N)+' '+str(K) +'\n'+str(num))


# write test cases
with open('testData/euler_08.txt', 'w') as file:
    for number in lines:
        file.write(str(number)+'\n')

# load the test file
with open('testData/euler_08.txt', 'r') as file:
    tests = file.readlines()

for k in range(1, len(tests)-1, 2):
    print(tests[k+1][:-1], tests[k].split(' ')[0], tests[k].split(' ')[1][:-1])
    largest_product(
        N  =int(tests[k].split(' ')[0]),
        K  =int(tests[k].split(' ')[1][:-1]),
        num=int(tests[k+1])
    )




# compute solutions
solutions = [
    largest_product(
        N  =int(tests[k].split(' ')[0]),
        K  =int(tests[k].split(' ')[1][:-1]),
        num=int(tests[k+1])
    ) for k in range(1, len(tests), 2)
]

with open('solutions/euler_08.txt', 'w') as file:
    for solution in solutions:
        file.write(str(solution)+'\n')
    