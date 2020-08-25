#The following iterative sequence is defined for the set of positive integers:
#   n → n</var>/2 (n is even)
#   n → 3n + 1 n is odd)
#Using the rule above and starting with n13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
#that all starting numbers finish at 1
#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

numbersallreadycalculation={
    1:1,
}
maxchaingenerator=3
collectallReturnNextCollatzNumber =[]

def ReturnNextCollatzNumber (n):
    collectallReturnNextCollatzNumber.append (n)
    #if numbersallreadycalculation.get(n):
    if n ==1:
        #b=0
        #for i in collectallReturnNextCollatzNumber:
            #numbersallreadycalculation[i]=len(collectallReturnNextCollatzNumber)+numbersallreadycalculation.get(n)-b
            ##if b==0:
                ##if numbersallreadycalculation(maxchaingenerator) < len(collectallReturnNextCollatzNumber) + numbersallreadycalculation.get(n): 
                    ##maxchaingenerator=n
            ##b=b+1
        return   collectallReturnNextCollatzNumber 
        #numbersallreadycalculation.get(n)
    #else:
        #collectallReturnNextCollatzNumber.append (n)

    elif (n % 2 !=0):
        return ReturnNextCollatzNumber (3*n +1)
    else:
        return ReturnNextCollatzNumber(int(n / 2))

for i in range (500_000,1_000_000):
    a= ReturnNextCollatzNumber(i)
    if len(a)>maxchaingenerator:
        maxchaingenerator=len(a)
        print (str(i ) + " "+ str(len(a)))
    collectallReturnNextCollatzNumber=[]

#for i in range (2,1_000_000):
    #ReturnNextCollatzNumber(i)
    #collectallReturnNextCollatzNumber=[]

#for i in numbersallreadycalculation:
    #if i<1_000_000 and    numbersallreadycalculation.get(i)>numbersallreadycalculation.get(maxchaingenerator):
        #maxchaingenerator=i
        #print (str(maxchaingenerator) + " " + str(numbersallreadycalculation.get(maxchaingenerator)))


#print (ReturnNextCollatzNumber(837799))
