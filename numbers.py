import math 
import random
x1=5
print("The ceil of",str(x1), "is: ",math.ceil(x1))
x2=23.5
print("The math floor of",str(x2) ,"is: ",math.floor(x2))
x3=2.12
print("The fabs is the absolute number of",str(x3), math.fabs(x3))
x4=12
print("The factorial of", str(x4) ,"is the highest value of : " ,math.factorial(x4))
x5=float(input("Enter a decimal or  int"))
x6=float(input("Enter a decimal or int "))
fmodmath= math.fmod(x5,x6)
print("The f mod of ",x5,'and', x6 ,"is", fmodmath)
x7=int(input("Enter a number "))
logcalculation= math.log2(x7)
print("The log calucation of ", str(x7), 'is: ', str(logcalculation) )
a1=1000
a2=1.06
pow= pow(a1,a2)
print("The power of ",a1 ,"and",a2, "is: ",pow )
print(random.randrange(2,12,5)) 
print(random.randrange(2,12,5)) 
print(random.randrange(2,12,5)) 
greeting=["Hi","Waagwaan","My G","Hey","What going on?" ]
results= random.choice(greeting)
print(results)

print(math.asin(1))