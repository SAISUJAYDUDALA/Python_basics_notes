# INPUT in python

name = input("name : ") #used for string 
print(name)

age = int(input("age : "))#used for int
print(age)

price= float(input()) #used for float 
print(price)


#Condition statements in Python
""" if - elif - else

    if(condition):
        statement1
    elif(condrion):
        statement2
    else:
        statementN
"""

food = input()
ans = "Yes" if food =="Cake" else "No"
print(ans)

print("sweet") if food == "Cake" or food == "Halwa" else print("not sweet")

"""clever if - we use []
    var = (false_val,true_val) [condition]
"""
age = int(input())
vote = ("NO","YES")[age>=18]
print(vote)


salary = int(input())
tax = salary*(0.1,0.2)[salary >=50000]  #here we dont know when to multiply with 0.1 or 0.2 so we use clever if, if it is more then 
print(tax)                              #50000 then we will do it with 0.2 if it is not then with 0.1                              
