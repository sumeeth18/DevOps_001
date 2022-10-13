#should import math module to work on math functions/ Keywords
from cmath import sqrt
import math
# working on some math functions 
# pow is nohing but x power of y wher x is value and y power vaslue, 
#eg:

x= input("enter x value")
y=input("enter y value")
X=int(x)
Y=int(y)

print(pow(X,Y))

#square root value of a number, syntax math.sqrt(X)
#eg:
a=input("enter value to get square root")
A=int(a)
print(float(math.sqrt(A)))

print(float((math.fmod(X,Y))))

