import numpy as np 
x = np.arange(10)
for n in np.nditer(x): 
    print(x)

a = np.arange(16)
a = a.reshape(4, 4) 
for x in np.nditer(a): 
    print(x) 

np.random.seed(0)
x1= np.random.randint(10, size=6 ) 
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))
print("x1 ndim is: ", x3.ndim)   
print(x3.shape) 
print(x3.size)
