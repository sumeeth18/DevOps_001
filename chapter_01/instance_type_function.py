# instance is testing which type of value it is
# type is also same function but instance is not preferable all the time

# execute the program and you would see ther data values and types


i = 7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1

a = 1
b = 'it a character'
c = 5.89
d = True
e = 93.8j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
