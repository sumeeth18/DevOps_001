# Data types collection are list set tuple
# list is a colllection of data in a square brackets separated by comma
# eg :

a = [1, 2, 3, 4]  # colection of integers in  list 'a'
b = ['hi', 'hello', 'welcome']  # string coolection
c = [1, 2, 'hi', 3]  # mixed list
d = [1, 1, 2, 2, [4, 5], 'hi']  # nest mixed list
a.append(5)
print(a)
a.remove(5)
print(a)

a.insert(2, 4)
print(a)
a.remove(2)
print(a)
print(len(b))
c.index(2)
print(d.count(1))
print(d.reverse())