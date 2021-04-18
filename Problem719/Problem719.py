##
#
#numbersalreadycalculated  ={
#    #1:1
##}
##
##maxchaingenerator =1 
##allnumbersfromagenerator=[]
##def  returnlengthchainfromgenerator(n):
#    #if numbersalreadycalculated.get(n):
#        #returnedvalue=len(#allnumbersfromagenerator)+numbersalreadycalculated.get(n)
        #for index,element in enumerate(#allnumbersfromagenerator):
#            numbersalreadycalculated[element]=returnedvalue-index
        #return len(allnumbersfromagenerator)+#numbersalreadycalculated.get(n)
#    allnumbersfromagenerator.append (n)
#    #if (n % 2 !=0):
#        #return returnlengthchainfromgenerator(3*n+1)
#    #else:
#        #return returnlengthchainfromgenerator(int(n/2))
#
#max=0
#for i in range (2,1_000_000):   #From 500_000 to 1_000_000 is enough
#    allnumbersfromagenerator=[]
#    #returnlengthchainfromgenerator(i)
#    #if #max< numbersalreadycalculated[i]:
#        #print (str(i) + "   ->  " + str(numbersalreadycalculated[i]))
#        #max =#numbersalreadycalculated[i]
#

#We define an $S$-number to be a natural number, $n$, that is a perfect square and its square root can be obtained by splitting the decimal representation of $n$ into 2 or more numbers then adding the numbers.
#For example, 81 is an $S$-number because $\sqrt{81} = 8+1$.<br />
#6724 is an $S$-number: $\sqrt{6724} = 6+72+4$. <br />
#8281 is an $S$-number: $\sqrt{8281} = 8+2+81 = 82+8+1$.<br />
#9801 is an $S$-number: $\sqrt{9801}=98+0+1$.
#Further we define $T(N)$ to be the sum of all $S$ numbers $n\le N$. You are given $T(10^4) = 41333$.
#Find $T(10^{12})$



#CheckifsplitSumIsSquare(8281,91,0)
#                                                            -------------------------------   
#                                                            |                             |
#                                                         -------------------------        |
#                                                         |  |                    |        |
#                                                         v  v                    v        v
#If I am checking 9801 the enter String of this function (1)(0)(1)(0) means 9*10^(1)+8*10^(0)+0*10^(1)+1*10^(0)
#and It returns 1000
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
encontrado=False
def dividir (inicio,strStar,orginal):
    global encontrado
    if encontrado:
        return True
    if len(strStar) ==1: 
        return False
    for i in range (1,len(strStar)):
        print (inicio+strStar)
        if encontrado:
            return True
        total = (inicio + " " + strStar[:i] +" "+strStar[i:])
        if check (total) ==(orginal):
            encontrado = True
            return True
        if len(strStar[i:])>1:
            dividir (inicio+strStar[:i],strStar[i:],orginal)
                
def check (texto):
    return (sum(int(i) for i in  texto.split(" ") if i.isnumeric()))

a=0
for i in range (1,(10**6)+1):
    
    encontrado=False    
    if (dividir ("",str(i**2),i)):
        print (str(i**2)+":Sí es:"+str(i) )
        a = a+(i**2)
    else:
        print (str(i**2)+":No es:"+str(i) )
print (a)
#if (dividir ("","6724", 82)):
    


