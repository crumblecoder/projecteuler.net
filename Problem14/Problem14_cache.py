

numbersalreadycalculated  ={
    1:1
}

maxchaingenerator =1 
allnumbersfromagenerator=[]
def  returnlengthchainfromgenerator(n):
    if numbersalreadycalculated.get(n):
        returnedvalue=len(allnumbersfromagenerator)+numbersalreadycalculated.get(n)
        for index,element in enumerate(allnumbersfromagenerator):
            numbersalreadycalculated[element]=returnedvalue-index
        return len(allnumbersfromagenerator)+numbersalreadycalculated.get(n)
    allnumbersfromagenerator.append (n)
    if (n % 2 !=0):
        return returnlengthchainfromgenerator(3*n+1)
    else:
        return returnlengthchainfromgenerator(int(n/2))

max=0
for i in range (2,1_000_000):   #From 500_000 to 1_000_000 is enough
    allnumbersfromagenerator=[]
    returnlengthchainfromgenerator(i)
    if max< numbersalreadycalculated[i]:
        print (str(i) + "   ->  " + str(numbersalreadycalculated[i]))
        max =numbersalreadycalculated[i]
