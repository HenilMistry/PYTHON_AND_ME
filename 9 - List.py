# list is the data type or data container for any type of data...
# list is ordered ...
# syntax of the list is shown below...
# a = [1,2,48,45] since it is ordered print(a) will result...1,2,48,45


a = [1,4,58,45]
print("list a : ",a) # printing list...
print("a[0] : ",a[0]) # accessing element using index values...
a[2] = 98 # changing values or manipulating using index...
print("after 'a[2]=98' list a : ",a)

# list with mixture of data types ...
b = [1,True,"Henil",215.512]
print("list b : ",b)

# slicing the list ... same as we have done it for string
print("a[:2] : ",a[:2])
print("a[::2] : ",a[::2])

# reverse the list without using method
print("b[::-1] : ",b[::-1])

"""
list methods .... 
sort() ... updates the list into ascending order ... doesn't return list
reverse() ... updates the list into descending order ... doesn't return list
append(<element>) ... add <element> at the end of list
pop(<index>) ... delete the <element> at <index>
insert(<index>,<element>) ... will add <element> at <index>
remove(<element>) ... remove <element> from last

for more functions
# https://docs.python.org/3/tutorial/datastructures.html use this link...

"""

# sort() method ...
a.sort()
print("after a.sort() a : ",a)
# print(a.sort()) # this is illegal or it will be null...

# reverse() method ...
a.reverse()
print("after a.reverse() a : ",a)

# append() method ...
a.append(45)
print("after a.append(45) a : ",a)

# pop() method ...
a.pop(4)
print("after a.pop(4) a : ",a)

# insert() method ...
a.insert(2,44)
print("after a.insert(2,44) a : ",a)

# remove() method ...
a.remove(44)
print("after a.remove(44) a : ",a)