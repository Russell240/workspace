import sys; 
a = [1, 2, 3, 4]
if (n := len(a)) < 5:
    print(f"List is too shoter ({n} elements, expected >=5)")

for number in range (1,10):
    if(number %2 ==0 ):
        print(number)
print(float(4.46/2))

pi =22/7 
radian= float(input('Radius of sphere in cm : '))
surfacearea= 4* pi*radian**2 
volume= (4/3) * (pi * radian**3)
print("Surface Area of the sphere  is: ", surfacearea, "cm2")
print("The Volume of the sphere is: ",volume, "cm3")


name = "python" 
print("p" in name) 
print("s" in name) 
print("o" not in name) 

age = 18 
requiredAge = 18 
print(age == requiredAge) 

FirstName="Alan"
FirstName="Not Given" if not FirstName else  FirstName 

list = [1,3,5,7,9,11,1 ]
i =0 
while i < len(list): 
    print(list)
    i = i + 1


x = True 
y = False 
print('x and y is' , x and y) 
print('x or y is' , x or y) 
print('not x is' , not x) 

orderquanity =int(input(("Enter number of orders: ")))
order_quanity = int(orderquanity)
if orders := 5 > order_quanity:
    print("Minimum  orders is 5")
