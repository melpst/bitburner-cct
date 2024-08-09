"""

    Find Largest Prime Factor
    You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


    A prime factor is a factor that is a prime number. What is the largest prime factor of 295788812?


    If your solution is an empty string, you must leave the text box empty. Do not use "", '', or ``.
"""


import math

def maxPrime(n, max):
    r = math.ceil(math.sqrt(n))
    num = list(range(2, n+1, 1))
    prime = list(range(2, r+1, 1))
    index = 0

    while index<len(prime):
        i = prime[index]
        prime = list(filter(lambda x: x%i!=0 or (x%i==0 and x==i), prime))
        index += 1

    if max:
        maxPrime = 2
        num.reverse()

        for n in num:
            isPrime = True
            for p in prime:
                if n%p==0 and n!=p:
                    isPrime = False
                    break
            if isPrime:
                maxPrime = n
                break
        return maxPrime
    else:
        prime.sort()
        x = n
        i = 0
        while i<len(prime):
            p = prime[i]
            if x%p==0:
                if x==p:
                    break
                else:
                    x = int(x/p)
                i = -1
            i += 1
        return x

# assert maxPrime(362077904, True) == 362077871
assert maxPrime(295788812, False) == 6722473
assert maxPrime(6722473, True) == 6722473
assert maxPrime(879228713, False) == 1931
# print(maxPrime(879228713, False))