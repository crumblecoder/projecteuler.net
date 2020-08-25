##The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
##Find the sum of all the primes below two million
#
#
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
##What is the 10 001st prime number?
#
#primes=[3,5,7,11,13]
#check =17
#find = 1999999
#while primes[-1]<find:
#    IsPrime=True
#
#    for i in primes:
#        if i> (check**(0.5)):
#            break
#        if ((check % i) == 0):
#            IsPrime = False
#    if IsPrime:
#        primes.append (check)    
#    check = check +2
#            
#
#print (sum(primes)+2-primes[-1])
##10474
#    

def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print (sumPrimes(2000000))