# # Arithematic operator 
# a = 37
# b = 28

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)


# # Relational operator 
# a=50
# b=37

# print(a == b)
# print(a != b)
# print(a <= b)
# print(a >= b)
# print(a<b)
# print(a>b)

# # Assignment Operator 
# num =37

# num += 10
# print(num)
# num -= 10
# print(num)
# num *= 10 
# print(num)
# num /= 10 
# print(num)
# num %= 10
# print(num)
# num **= 10 
# print(num)



# #  Logical operator 
 
 
#  #logical not 
# print(not True)
# print(not False)
 
#   #logical and 
# val1 = True
# val2 = True
# print("and operator:",val1 and val2)

# # logical OR
# val1 = False
# val2 = True
# print("and operator:",val1 or val2)

# # Type conversion 
#  # implicit conversion 
# a=2 
# b=3.234
# sum=a+b
# print(sum)

# # Type Casting
#  # Explicit conversion 

# a,b = 2,"3"
# c=int(b)
# print(a+c)

#Input in python 

# name=input("enter you name :")  
# print("welcome ",name) #result will always be string.We will have to do the type casting in order to change the data type. See the below example 

# age = int(input("enter your age :"))
# print("you entered :",age) # we are checking the data type below
# print(type(age))

#simple code for taking inpput our name age and date of birth

name=input("enter your name:")
print("welcome",name)
age=int(input("enter your age :"))
print("your age is :",age)
DOB=str(input("enter you date of birth:"))
print("i wil wish you on ",DOB)
