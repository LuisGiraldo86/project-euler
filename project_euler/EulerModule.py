def eratosthenes_sieve(N:int)->list:

    # pseudo-code from https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    
    prime = 2
    ind_primes = [True]*(N+1)
        
    while prime**2 <= N:
        if ind_primes[prime]:
            for k in range(prime**2, N+1, prime):
                ind_primes[k]=False
        prime+=1

    ind_primes[0]=False
    ind_primes[1]=False
        
    return ind_primes

def prime_divisors(N:int, sieve:list)->dict:

    divisors = {}
    if N == 1: return divisors
    else:
        for k in range(2,len(sieve)):
            if sieve[k]:
                while N%k== 0:
                    if str(k) in divisors.keys():
                        divisors[str(k)]+=1
                    else: divisors[str(k)]=1
                    N = N//k
            if N==1:break
    if len(divisors)==0:divisors[str(N)]=1
    return divisors

def sum_proper_divisors(n:int)->int:
    
    sum_div = 1
    div = 2
    while div**2 <= n:
        quot, rem = divmod(n, div)
        if rem == 0:
            sum_div += div
            if quot != div: # for perfect squares
                sum_div+=quot
        div+=1
    return sum_div

def count_divisors_with_bool(N:int, sieve:list)->int:

    """
    Count the total number of divisors given a list with True in the prime positions and False in the composite positions
    """
    
    total = 1
    if N == 1: return total
    else:
        for k in range(2,len(sieve)):
            if sieve[k]:
                count=0
                while N%k == 0:
                    count+=1
                    N = N//k
                total = total*(count+1)
            if N==1:break
    if total==1:total=2
    return total

def count_divisors_with_primes(N:int, primes:list)->int:

    """
    Count the total number of divisors given a list of prime numbers
    """

    total = 1
    if N == 1: return total
    else:
        for prime in primes:
            count=0
            while N%prime == 0:
                count+=1
                N = N//prime
            total = total*(count+1)
            if N==1:break
    if total==1:total=2
    return total
