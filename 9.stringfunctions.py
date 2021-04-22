story = "once upon a time there was a guy named harry who uploaded virus on our office network!"
#string functions
print(len(story))
print(story.endswith("network!"))
print(story.count("on"))
print(story.capitalize())
print(story.find("who"))
print(story.replace("harry", "ali"))


###ESCAPE SEQUENCES \n-newline \t tab \' singlequote \\ backslash

meow = "harry is good. \n \t he is very\'good\\"
print(meow)
