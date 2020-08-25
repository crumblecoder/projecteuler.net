#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

primes=[3,5,7,11,13]
check =17
find = 10000
while len(primes)<find:
    IsPrime=True

    for i in primes:
        if i> (check**(0.5)):
            break
        if ((check % i) == 0):
            IsPrime = False
    if IsPrime:
        primes.append (check)    
    check = check +2
            
print (primes[-1])


#104743
