"""lists is a buit-in datatype that stores set of values
    it can store elements of different types(integer, float, string, etc)
"""

marks = [12.3,33.4,55,6]
print(marks)
print(type(marks))
print(marks[0])

"""in python
    string are inmmutable (which can not be changed) access
    lists are mutable ( which can be changed) access , Change
"""
print(len(marks)) #prints length of the list

#list slicing 
# similat to sting slicing
# list_name[ starting_idx : ending_idx] ending will not be included

print(marks[1:3])
print(marks[-3 : -1])

list = [2,1,3]
list.append(4) # add one element at the end
print(list)

list.sort() # sorts in ascending order
print(list)

list.sort(reverse=True) # sort in descending order
print(list)

list.reverse() # print list in reverse 
print(list)

list.insert(1,5) # inserts a value at the given index insert(index,value)
print(list)

list.remove(1) # removes frist occurrence of element
print(list)

list.pop(3) # removes element at idx pop(index)
print(list)


list = ["m" , "a", "a","m"]
copy_list = list.copy()

copy_list.reverse()
if(list == copy_list):
    print("palendrome")
else:
    print("not a palendrome")    
