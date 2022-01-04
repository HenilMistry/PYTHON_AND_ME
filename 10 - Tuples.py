# tuples is also a data container same as the list
# only the difference is that you cannot modify data in tuples

a = (4,7,8,21,0,21,1,4,21) # tuple created...
print("a : ",a)
b = () # empty tuple...
print("b : ",b)
# c = (1) # this will not taken as a tuple
print("syntax c = (1) will not create tuple, we need to do c = (1, ) to make tuple with one element : ")
c = (1,) # this is right way to declare tuple containing only 1 member...
print("c : ",c)

"""
tuples method...

count(<element>) ... return the number of times the <element> is occurred in tuple
index(<element>) ... return the index of first occurrence of the <element> in the tuple

for more functions...
# https://docs.python.org/3/c-api/tuple.html use this link...

"""

# count() method ...
print("a.count(5) : ",a.count(5))
print("a.count(21) : ",a.count(21))
print("a.index(21) : ",a.index(21))

# assignment 2 was solved from here ... ===============================================================================
# 1) tuples with different data types
print("\n\nQuestion-1")
a = (1,2,3,7,45) # tuples with integer
b = ("Henil","Mistry","Rakeshbhai") # tuple with string
c = (1.51,215.5,88.9) # tuple with floating numbers
print("a : ",a,"\nb : ",b,"\nc : ",c) # printing all tuples...

# 2) tuples with number and printing one item...
print("\n\nQuestion-2")
# tuples with number is already created...
print("a[2] : ",a[2])

# 3) add an item in tuple...
print("\n\nQuestion-3")
# here one thing needs to be noticed thet tuples are immutable but we can modify by converting it into list...
A = list(a)
A.append(77)
a = tuple(A)
print(a)
# we can modify a tuple by moderator as list ...

# 4) convert a tuple to string...
print("\n\nQuestion-4")
FullName = ' '.join(b) # using join method to converting a tuple into string...
print("after \"FullName = ' '.join(b)\" FullName : ",FullName)

# 5) find a length of a tuple
print("\n\nQuestion-5")
print(len(b)) # using len() method ...
