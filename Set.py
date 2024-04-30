"""set is the collection of the unirdered items
   each element in the set must be unique & immutable

   we can store int,float,str,tupple,boolean datatypes in the set but not dictionary or lists
   as they are mutable 

   if we try to add we will get a error "unhashable type error"
   unhashable - dictionary , lists
"""

collection = {1,2,3,4,"hello","hello",4}

print(collection)
print(len(collection)) 

null_set  = set() # this is the syntax for creating empty set
"""
    if can not create a empty set in the following way
    null_set = {}
    because it is similar to creating a empty dictionary
    null_dic = {}

    so we can only create a empty set by null_set = set()
    
"""
set = collection
set2 = {3,4,5}
# here in the set we can add or remove the values but we cannot manipulate the values like lists and dictionary

set.add("element") # adds an element
print(set)

set.remove("element") # removes the element
print(set) # if there is no element in the set we will get a key error

set.clear() # empities the set

set.pop() # it will randomly pop an element out of the set

print(set.union(set2)) # prints a new set which is combitaion of both set and set2

print(set.intersection(set2)) # print a new set which is combined common values in both set and set2
