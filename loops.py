"""
    while loop 

    while condition:
        #some work 
"""
nums =[1,4,9,16,25,36,49,64,81,100]
heroes=["ironman","thor","superman","batman"]

i=0    # intialization
while i < len(heroes):
    print(heroes[i])
    i= i+1 #i += 1 

print(nums.index(16))  # to find the index of the value in the list 


i = 0 
while i <= 5:
    if (i == 3):
        print("found at 3")
        break  # it will terminate the loop here
    else:
        print("finding..")   
    i = i + 1    


i = 0 
while i <= 5:
    if (i == 3):
        i = i+ 1
        continue # it will skip this part of the loop here
        
    print(i)   
    i = i + 1   

"""
    for loops are used for sequential traversal. for traversing list,string,tuples etc.
"""

num = (1,2,3,4,5,6,7,8,9) # tuple
veg = ["allu","carrot","tomata","curry"]

for val in num:
    print(val)

for val in range(len(num)):  # it is another way to write the for loop
    print(val ,  end = " ") 
"""
   (i , end = " ") is used to print the output in same line
   (i , end = "\n")is used to print the output in new line
"""

print(*veg)


for val in veg:
    print(val)   

"""
    in pyton we can use else after for loop like
    for .....:
        .....
    else:
        .....

    when we write else it will print the code which is in the else after the out put of the for loop
    it is same as writing print statement at the end

    but it is useful when we write break statement in the code        
"""     

str = "saisujaydudala"

for char in str:
    if(char == 'y'):
        print("Y found")
        
    print(char)
else:
    print("END")    # similar to just typing print("END") at the end of the statement



# in the above case it will print all the char and at end it will print END

str = "abhinaydudala"

for char in str:
    if(char == 'y'):
        print("Y found")
        break
    print(char)
else:
    print("END")   

# in this u can see it will only print upto the condtion and break and will not print else statement unlike the above
   

# range ()
"""
    range function in for loop helps to return a sequence of numbers, starting from 0 by default, and increments by 1(by default)
    and stops before a specified number.

    range(start?,stop,step?)
"""
print("..................................................................................")

for i in range(5):
    print(i,end = " ")
print("\n")
for i in range(0,10):
    print(i,end=" ")
print("\n")
for i in range(0,20,2):
    print(i,end=" ")    



"""
    pass statement:
    pass is a null statement that does nothing. it is used as a placeholder for future code
"""   

for i in range(5):
    pass            # here if we wite pass it will skip the whole for loop but we keep any other like break , continue ..etc it will error

print("something else")

