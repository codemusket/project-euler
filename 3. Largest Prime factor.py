'''
Largest prime factor

ProjectEuler.net Problem 3. 8/9/15

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''


primes = []
factors = []

num = 600851475143 

def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def primefactors():
    for i in range(1, num):

        if isprime(i):
            if num % i == 0:
                factors.append(i)
                print(i)
    return max(factors)

def fastprimefactors():
    target = 600851475143

    i = 2
    while target != 1 :
        
        if target % i == 0:
            target /= i
            print(target)
        i += 1


    print(i)
