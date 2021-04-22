"""
Write a program to store seven fruits in a list entered by the user.
Write a program to accept marks of 6 students and display them in a sorted manner.
Check that a tuple cannot be changed in Python.
Write a program to sum a list with 4 numbers.
Write a program to count the number of zeros in the following tuple:
"""


# 1st
f1 = input("Enter a fruit number 1:")
f2 = input("Enter a fruit number 2:")
f3 = input("Enter a fruit number 3:")
f4 = input("Enter a fruit number 4:")
f5 = input("Enter a fruit number 5:")
f6 = input("Enter a fruit number 6:")
f7 = input("Enter a fruit number 7:")
fruit = [f1,f2,f3,f4,f5,f6,f7]
print(fruit)

#2nd

s1 = input("Enter the total marks of student 1:")
s2 = input("Enter the total marks of student 2:")
s3 = input("Enter the total marks of student 3:")
s4 = input("Enter the total marks of student 4:")
marks = [s1,s2,s3,s4]
marks.sort()
print(marks)


#3
t = (1,2,3,4,5)
print(t)
###t[0] = 6
print(t)

#4
c1 = int(input("enter a number for sum:"))
c2 = int(input("enter another number to the total:"))
c3 = int(input("enter another number to the total:"))
sum = (c1+c2+c3)
print(sum)

#5
a = [0,1,2,3,0,4,0,5]
print(a.count(0))



























