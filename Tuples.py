""" a built in data type that lets us create immutable sequence of values
"""

tup = (2,1,3,1)
print(tup[0])

tup = () # here we can take a empty tuple 
print (tup)
print(type(tup))

tup = (1,)
print(tup)
print(type(tup))

"""
    we can create a single valued tupple only by keeping coma after the value other wise we will get error
    if we give (1) it will be a int datatype not tupple like wise (1.3) is float not tupple and ("tp s d") is a string not tupple
    for multiplue values we have a option to either keep it or not but for single value we should use coma after the value
"""
print(tup[:3])

print(tup.index(1)) # returns index of the frist occurrence
print(tup.count(1)) # counts total occurrences


 