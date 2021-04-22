''''''
'''Write a Python program to display a user-entered name followed by Good Afternoon using input() function.
Write a program to fill in a letter template given below with name and date.
letter = ‘’’ Dear <|NAME|>,

                        You are selected!

                        <|DATE|>

Write a program to detect double spaces in a string.
Replace the double spaces from problem 3 with single spaces.
Write a program to format the following letter using escape sequence characters.
letter = “Dear Harry, This Python course in nice. Thanks!!”
'''

#1
a = input("Enter a name : ")
print("Good Morning,", a)


#2
letter =  "Dear <|NAME|>,
You are selected!
 <|DATE|>"

name = input("Enter a name :\n")
date = input("Enter date  :\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)

#3
e = "The  string with double spaces"
double = e.find("  ")
print(double)

#4
e1 = "The  string  with  double   spaces"
double1 = e1.find("  ")
print(e1)
double1 = e1.replace("  ", " ")
print(double1)

#5
letter = "Dear harry, \n \t This Python course in nice. \nThanks!!"
print(letter)