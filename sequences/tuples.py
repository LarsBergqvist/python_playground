#!/usr/bin/env python3

#
# Examples on tuple usage
#

# Cartesian product M x N
M = "AB"
N = "12"

# Unpack with dummy variable _
product = ((m,n) for m in M for n in N)
for m, _ in product:
    print(m)

# Unpack with dummy variable _
product = ((m,n) for m in M for n in N)
for _ , n in product:
    print(n)

#
# Unpacking tuple with *
#
my_tuple = (1,2,3)
print(my_tuple)

def multiply_values(a,b,c):
    return a*b*c

# Have to unpack the tuple to use with method that takes three values
result = multiply_values(*my_tuple)
print(result)


#
# Grab rest with *
#
a, b, *rest = range(1, 5)
print(a)
print(b)
print(rest)

*rest, a, b = range(1, 5)
print(a)
print(b)
print(rest)

a, *rest, b = range(1, 5)
print(a)
print(b)
print(rest)
