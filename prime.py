"""

    Find Largest Prime Factor
    You are attempting to solve a Coding Contract. You have 10 tries remaining, after which the contract will self-destruct.


    A prime factor is a factor that is a prime number. What is the largest prime factor of 295788812?


    If your solution is an empty string, you must leave the text box empty. Do not use "", '', or ``.
"""

import math
import cProfile

def flooredRoot(num):
    return math.floor(math.sqrt(num))

# assert flooredRoot(0) == 0
# assert flooredRoot(1) == 1
# assert flooredRoot(2) == 1
# assert flooredRoot(3) == 1
# assert flooredRoot(4) == 2
# assert flooredRoot(5) == 2
# assert flooredRoot(8) == 2
# assert flooredRoot(9) == 3
# assert flooredRoot(11) == 3
# assert flooredRoot(15) == 3
# assert flooredRoot(16) == 4

def possibleFactorRange(num):
    if num<4:
        return [num]
    else:
        return list(range(2, flooredRoot(num)+1))

# assert possibleFactorRange(0) == [0]
# assert possibleFactorRange(1) == [1]
# assert possibleFactorRange(2) == [2]
# assert possibleFactorRange(3) == [3]
# assert possibleFactorRange(4) == [2]
# assert possibleFactorRange(5) == [2]
# assert possibleFactorRange(9) == [2,3]
# assert possibleFactorRange(11) == [2,3]
# assert possibleFactorRange(16) == [2,3,4]

def possibleLargestRange(num):
    return list(range(2, num+1))

# assert possibleLargestRange(0) == []
# assert possibleLargestRange(1) == []
# assert possibleLargestRange(2) == [2]
# assert possibleLargestRange(3) == [2,3]
# assert possibleLargestRange(4) == [2,3,4]
# assert possibleLargestRange(5) == [2,3,4,5]
# assert possibleLargestRange(9) == [2,3,4,5,6,7,8,9]
# assert possibleLargestRange(11) == [2,3,4,5,6,7,8,9,10,11]
# assert possibleLargestRange(16) == [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def sieveRecursive(range, mod):
    if range == []:
        return [mod]
    else:
        possiblePrime = list(filter(lambda x: x%mod != 0, range))
        prime = [mod]

        if len(range)-len(possiblePrime)<=1:
            return prime+possiblePrime
        else:
            return prime+sieveRecursive(possiblePrime[1:], possiblePrime[0])

# assert sieveRecursive([], 2) == [2]
# assert sieveRecursive([3], 2) == [2,3]
# assert sieveRecursive([3,4,5], 2) == [2,3,5]
# assert sieveRecursive([3,4,5,6,7], 2) == [2,3,5,7]
# assert sieveRecursive([3,4,5,6,7,8,9,10], 2) == [2,3,5,7]
# assert sieveRecursive([3,4,5,6,7,8,9,10,11], 2) == [2,3,5,7,11]
# assert sieveRecursive([3,4,5,6,7,8,9,10,11,13], 2) == [2,3,5,7,11,13]

def largestFactor(num, range):
    if num%range[-1]==0:
        return range[-1]
    elif num in range:
        return num        
    else:
        for p in range:
            if num%p == 0:
                new = int(num/p)
                if new == 1:
                    return p
                return largestFactor(new, range)
        return num
    
# assert largestFactor(2, [2]) == 2
# assert largestFactor(2, [2,3]) == 2
# assert largestFactor(3, [2,3]) == 3
# assert largestFactor(4, [2,3]) == 2
# assert largestFactor(9, [2,3,5,7]) == 3
# assert largestFactor(121, [2,3,5,7,11]) == 11
# assert largestFactor(21, [2,3,5,7,11]) == 7

def largestPrimeFactor(num):
    range = possibleFactorRange(num)
    prime = sieveRecursive(range[1:],range[0])
    return largestFactor(num, prime)

# print(largestPrimeFactor(352806313))

# assert largestPrimeFactor(2) == 2
# assert largestPrimeFactor(3) == 3
# assert largestPrimeFactor(4) == 2
# assert largestPrimeFactor(5) == 5
# assert largestPrimeFactor(7) == 7
# assert largestPrimeFactor(9) == 3
# assert largestPrimeFactor(11) == 11
# assert largestPrimeFactor(13) == 13
# assert largestPrimeFactor(16) == 2
# assert largestPrimeFactor(2193688) == 911
# assert largestPrimeFactor(62509998) == 2347
# assert largestPrimeFactor(424826643) == 7229
# assert largestPrimeFactor(302481900) == 19
# assert largestPrimeFactor(777259326) == 12647

# assert largestPrimeFactor(295788812) == 6722473
# assert largestPrimeFactor(879228713) == 1931
# assert largestPrimeFactor(209632533) == 22447
# assert largestPrimeFactor(851294011) == 399481
# assert largestPrimeFactor(834713741) == 7801063
# assert largestPrimeFactor(352806313) == 17939


def largestPrime(num):
    range = possibleFactorRange(num)
    prime = sieveRecursive(range[1:],range[0])

    numRange = reversed(possibleLargestRange(num))
    for n in numRange:
        divisor = list(filter(lambda x: n%x==0 and n!=x, prime))
        if len(divisor)==0:
            return n
    return num

# assert largestPrime(2) == 2
# assert largestPrime(3) == 3
# assert largestPrime(4) == 3
# assert largestPrime(5) == 5
# assert largestPrime(7) == 7
# assert largestPrime(9) == 7
# assert largestPrime(11) == 11
# assert largestPrime(13) == 13
# assert largestPrime(16) == 13

# assert largestPrime(362077904) == 362077871
# assert largestPrime(6722473) == 6722473

# def maxPrime(n):
#     r = math.ceil(math.sqrt(n))
#     num = list(range(2, n+1, 1))
#     prime = list(range(2, r+1, 1))
#     index = 0

#     while index<len(prime):
#         i = prime[index]
#         prime = list(filter(lambda x: x%i!=0 or (x%i==0 and x==i), prime))
#         index += 1

#     maxPrime = 2
#     num.reverse()

#     for n in num:
#         isPrime = True
#         for p in prime:
#             if n%p==0 and n!=p:
#                 isPrime = False
#                 break
#         if isPrime:
#             maxPrime = n
#             break
#     return maxPrime

# assert maxPrime(362077904) == 362077871
# assert maxPrime(6722473) == 6722473



# cProfile.run('maxPrime(4294967297)')
# cProfile.run('largestPrime(4294967297)')