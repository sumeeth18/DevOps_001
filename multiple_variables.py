# we assign several variable to several values in a single line\
# but nopo of variables = no of values
# valid one
a, b, c = 1, 2, 3
print(a, b, c)
aa, bb, _ = 4, 5, 6
print(aa, bb)

# invalid one
a, b, c = 1, 2, 3
print(a, b)  # it throw error

c, d, e = 1, 2
print(c, d, e)
