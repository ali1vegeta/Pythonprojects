#lists and tuples
#lists are container to store a set of values of an data  types

# Create a list
a = [1,2,3,4,5]
# Print the list using print()
print(a)

# Access using index using a[0], a[1], a[2]
print(a[2])
# Change the value of a particular object from list a[0], a[1], a[2]
a[0] = 98
a[1] = 99
print(a)

# We can create a list with items of different data types
c = [45, "Harry", False, 6.9]
print(c)

#slicing
friends = ["harry","rohan","sam","vik","monica","divya"]
print(friends[0:4])
print(friends[-3:])

#Sorting
sort = [1,3,2,4,6,7,9,8,5]
sort.sort()
print(sort)
sort.reverse()
print(sort)
sort.append(10)
print(sort)
sort.insert(4,5)
print(sort)
sort.pop(4)
print(sort)
sort.remove(9)
print(sort)



#############TUPLES
#Creating a tuple
t = (1,2,4,5,1)
print(t[0])

# Cannot update tuple value
# t[0]= 34   #will give error u cant update a tuple
print(t)

#tuple methods
print(t.count(1))
print(t.index(5))

