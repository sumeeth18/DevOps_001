# Different types of data types in python
# boolean:- ;boolean is also an integer and which indicates true or false

a = 10
b = 20
if a == b:
    print(True)
else:
    print(False)

    # Number are nothing but integers

a = 10  # where 10 is an integer value

# floating point number which are having deciamal value

b = 5.8

# complex number

c = 10j

print(a)
print(b)
print(c)

# string value
name = 'variable name'

print(name)

# tuple an order collection of n values(n>=0)
# immutable and they are not hashable
at = (1, 2, 3)
bt = (1, 'a', 'python', (1, 2))
print(at)
print(bt)

# list a set of collection in a sqaure braackets
# its  mutable and hasable
al = [1, 2, [11, 22], 3, 'python']
al[2] = [33, 44]
print(al)

# set : an unorder collections in a curly braces(n>=0)
# unhasable
askir = {1, 2, 'a'}
bs = {3, 'b'}
print(bs)

# dict:an unorder collection of unique value

ad = {1: 'one',
      2: 'two'}
print(ad)
