"""Write a Python program to add two numbers.
Write a Python program to find the remainder when a number is divided by Z(Integer).
Check the type of the variable assigned using the input() function.
Use a comparison operator to find out whether a given variable a is greater than b or not. (Take a=34 and b=80)
Write a Python program to find the average of two numbers entered by the user.
Write a Python program to calculate the square of a number entered by the user."""


print("program to add two numbers")
a = input("enter a number : ")
a = int(a)
b = input("enter a number : ")
b = int(b)
print("Sum is :", a+b )


print("program to find the remainder")
b = 45
c = 16
print(" the remainder when a is divided by b is : ", a%b )

print("program to find average")
d = 6
e = 18
f = d+e
print("the avg is : ", f/2 )

print("program to see if one variable is greater and other")
g = int(input("Enter the number :"))
h = int(input("Enter the number :"))
i = (g>h)
print(i)


j = int(input("Enter a num : "))
print("The square of a number is : ", j*j)

