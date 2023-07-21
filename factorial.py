import numpy
n=int(input("Enter a number: "))
x=numpy.prod([i for i in range(1,n+1)])
print(x)