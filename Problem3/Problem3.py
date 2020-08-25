#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

mynumber = 600851475143
init =int (600851475143 **(0.5))+1

def Isprime(n):
    if n == 0 or n ==1:
        return False
    for i in range (2,int(n ** (0.5))+1):
        if  (n % i )==0:
            return False    
    return True

            
while ( init > 3):
    if ( mynumber % init)==0 and Isprime(init):
        print (init) 
        break
    init = init -1


