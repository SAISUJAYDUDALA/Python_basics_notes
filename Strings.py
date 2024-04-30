str1 = "this is a string"
str2 = 'HI'
str3 = """this is sujay"""

str1 = "this is a string. \n we are creating it in python"
print(str1) #hrere \n is a escape sequence characters which helps to print the line in next line
# \t for giving a tabspace between them

str1 = "sai"
str2 = "sujay"
print(str1+" "+str2) #concatnation
print(len(str1+" "+str2))

str = "SAI SUJAY"
print(str[2])
# here in python we can only asscess the data in the index but we cannot manipulate the data in the index like str[3] ="@"
# this will show the error 'str' object does not support item assignment


#slicing  str[starting_idx : ending_idx] here ending idx is not included

str = "ApnaCollage"
print(str[1:4])
print(str[:4]) # here python will automatically knows that we need to start from the frist index
print(str[4:]) # here python will automatically knows that we need to run this upto the last index

"""here in pythin we there is a future that it can also count the string in backward using negitive indexing"""

str = "Apple"
print(str[-3:-1]) # here also it will only print -3,-2 but not -1

str = " i am a coder."

print(str.endswith("er.")) # returns true if string end with substr
print(str.capitalize())#capitalizes 1st char here it will only work one time 
                        #if u want it to change permenently do str = str.capitalize()

print(str.replace("a","A")) #replaces all occurrence of old with new
print(str.find("am")) #returns 1st index of 1st occurrence
print(str.count("a") )#counts the occurrence of substr in string
