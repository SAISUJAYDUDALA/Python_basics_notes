""" 
type conversion is nothing but converting a datatype of a varible to another datatype like from int to float ..etc
it is basically two types  type_converstion and the other one is type_casting 

in type_converstion python interpeter will automaticlly convert the type 
in type_casting we should manually convert the type 
"""

#type converstion 
 
a = 2
b = 4.35

print(a + b) # here python will print the output value in the float because it is superior than the int 


#type casting 
a = "S"
b = 4.35

#print(a + b) # here it will show a error "can only concatenate a string (not "float") t0 string"

a = int("2")  # here it is typecasting we should mentioned the datatype to which we want to convert
b = 4.35

print(type(a))
print(a + b)

a = 3.31
b = str(a)

print(type(b))# here it will print string