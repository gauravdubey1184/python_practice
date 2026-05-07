# print("hello Gaurav")

##sum of two numbers
# a = int(input("enter first number"))
# b = int(input("enter second number"))
# print("sum is", a+b)

# # squre of numbers
# num = int(input("enter your number:"))
# print("squere root of this number:", num * num)

# calculator
# a = int(input("enter first number:" ))
# b = int(input("enter second number:"))
# print("addition is :", a+b)
# print("subtraction is :", a-b)
# print("multiply is :",a*b)
# print("division is :",a/b)

# problem: age after 5 years
# name =input("enter your name:")
# age = int(input("enter your age:"))
# print("hello", name , "your age will be", age + 5, "after 5 year")

# type conversion trick hera a value is string and b is integer so here we want add a and b so here we are convert a into interger 
# a = "50"
# b = 20
# print(int(a) + b)

# tricky question here a and b is string that's why sting will be join not add
# a = "10"
# b = "20"
# print(a+b)

# a = int(input("enter first number"))
# b = int(input("enter second number:"))
# c = int(input("input third number:"))
# print("average is:", (a+b+c)/3)

# a = int(input("enter your number"))
# print("the cube is of:", a*a*a)

# a = "10"
# b = "7"
# print(int(a) + int(b))
# print(a+b)

# if else practice
# number = 10
# if number > 5:
#     print("greater")
# else:
#     print("smaller")

# even odd
# num = int(input("enter any number:"))
# if num % 2 == 0:
#     print("even")
# else:
#     print("odd")

# pass fail
# marks = int(input("enter marks:"))
# if marks >= 40:
#     print("pass")
# else: print("fail")

# multiple condition
# marks = int(input("enter your marks:"))
# if marks >= 80:
#     print("Grade A")
# elif marks >= 60:
#     print("Grade B")
# else:
#     print("Grade C")

# loop
# for i in range(5):
#     print(i)

# num = int(input("enter any number:"))
# for i in range (1,11):
#     print(num * i)

# sum of numbers
# total = 0
# for i in range(1, 6):
#     total = total + i
#     print("sum:", total)

# while loop
# i = 1
# while i <=5:
#     print(i)
#     i = i + 1

# print even number
# for i in range(1,10):
#     if i % 2 == 0:
#         print(i)

# check number is positive negetive or zero
# num = int(input("enter number:"))
# if num > 0:
#     print("number is positive")
# elif num < 0:
#     print("number is negetive")
# else:
#     print("number is zero")

# print number 1 to 10 by using loop
# for i in range(1,11):
#     print(i)

# table with loop
# num = int(input("enter your number:"))
# for i in range(1,11):
#    print(i * num)

# even odd using if and loop
# for i in range(1,101):
#     if i % 2 == 0:
#      print("even numbers are:", i)

# for i in range(1,101):
#     if i % 2 == 0:
#         print("even numbers are:", i)
#     else:
#         print("odd numbers are :", i)


# factorial number
# num = int(input("enter any number:"))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i
#     print("factorial is : ", fact)
    
#odd numbers
# for i in range(1,101):
#     if i % 2 != 0:
#         print("odd number are:", i)

# odd even number
# for i in range(1, 101):
#     if i % 2 == 0:
#         print("even numbers are:", i)
#     else:
#         print("odd numbers are:" , i)

#prime number
# for num in range(2, 101):
#     prime = True
#     for i in range(2, num):
#         if num % i ==0:
#             prime = False
#             break
#     if prime:
#         print(num)

# num = int(input("enter any number"))
# for i in range(1, 11):
#     print(i * num)

# for i in range(1,21):
#     if i % 2 == 0:
#         print("even numbers: ", i)
#     else:
#         i % 2 != 0
#         print("odd numbers:", i)

num = int(input("enter any number"))
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negetive")
else:
    num = 0 
    print("number is zero")