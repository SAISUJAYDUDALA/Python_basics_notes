"""
    Dictionaries are used to store data values in key:value pairs
    They are unordered, mutable(changeable) & don't allow duplicate keys
"""
info = {
    "key" : "value",
    "name" : "sai sujay",
    "learning" : "coding",
    "age" : 21,
    "is_adult" : True,
    "marks" : 94.3,

    "subjets" :["python","C","jave"],# set datatype
    "topic" : ("dict","set")   #tuple datatype
} 
"""we can take any type of datatype in the "values" but when it comes to "keys" we can only take int,char,string,float,BOOLEN"""

print(info)

print(info["name"])

info["name"] = "Abhinay"  #to update the value
info["surname"] = "Dudala"#to add a new key and value in the dictonary


null_dict = {}
print(null_dict)



#nested dictionaries

student ={
    "name" : "sujay",
    "subjects" : {
        "phy" : 95,
        "chem" : 55,
        "math" : 12
    }
}

print(student)
print(student["subjects"]) #to access subjects which is under the student
print(student["subjects"]["chem"]) # to access nestes dictonaries we will use another square brackets

print(student.keys()) # it will return all keys in the dictonary
print(student.get("key")) # it will aslo give the value for the wanted key

"""
    the difference btw student["key"] and student.get("key") is
    if there is a pre-exciting data in the dictionary then 
    student["key"] --> value #output
    student.get("key") --> value # output

    but if there is no pre-exciting data in the dictionary then 
    student["key"] --> error # output
    student.get("key") --> none # output
"""
 
print(student.values()) # it will returns all values in the dictionary
print(student.items())  # it returns all the (key, value) pairs as a tuple
print(student.update({"city" : "delhi"})) # it is used to add a key value pair
