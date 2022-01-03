# set is a collection of non-repetitive data
# syntax is similar to dictionary but without ':'

SET = {1,2,3,1}
print(SET) # repeated values will not be there even if inserted

a = {} # this will create empty dictionary...
print("type(a) : ",type(a))
b = set() # this will create empty set...
print("type(b) : ",type(b))

"""
methods of set

Len(<set>) ... return the length of the <set> passed in argument
remove(<element>) ... delete the <element> from the set
pop() ... remove arbitrary the element from set and return that element
clear() ... empties the set
union() ... returns union of the sets
intersection() ... returns the intersection of sets
add() ... adds element in the set

--> tuples can be added as element in set but not list and dictionary...
--> only hashable objects can be added to set... 

"""

# declared two sets...
a = {1,2,5,8,10}
b = {'henil','rakeshbhai','mistry'}

# printing two sets
print("a : ",a,"\nb : ",b)

# printing length of two sets
print("length of a : ", len(a),"\nlength of b : ",b)

# remove() method...
a.remove(5)
print("after a.remove(5) a : ",a)

# b.pop()
# pop() method...
print("b.pop()  : ",b.pop())

# clear() method ...
b.clear()
print("after b.clear() b : ",b)

# declaring b for performing union and intersection with a...
b = {8 , 9 , 5 , 10 , 100}
print("a : ",a," b : ",b)
c = a.union(b)
print("after c = a.union(b) : ",c)
c = a.intersection(b)
print("after c = a.intersection(b) c : ",c)

# assignment 2 was solved from here ===================================================================================
# 1) adding a member in set and clearing a set
print("\n\nQuestion - 1")
setX = {1,2,3}
print("before any operation setX : ",setX)
setX.add(5)
print("after setX.add(5) setX : ",setX)
setX.clear()
print("after setX.clear() setX : ",setX)

# 2) removing a element from set if it exist
print("\n\nQuestion - 2")
setY  = {50,54,60,64,70,74}
print("setY : ",setY)
# setY.remove(80) # this will throw error if element passed as argument is not a member of a set...
setY.discard(80) # simply use this method rather than using remove() method...
# discard() method will remove element if it exist in set...
print("after setY.discard(80) setY : ",setY)

# 3) insertion , union, difference of set
print("\n\nQuestion - 3")
a = {1,2,5,8}
b = {5 , 7 , 9 , 4}
c = {10, 1 , 8 , 9}
ans = {}
print("a : ",a," b : ",b," c : ",c," ans : ",ans)
# union ...
ans = a.union(b)
print("after ans = a.union(b) : ",ans)
# intersection ...
ans = b.intersection(c)
print("after ans = b.intersection(c) : ",ans)
# difference ...
ans = c.difference(a)
print("after ans = c.difference(a) : ",ans)

# 4) finding maximum and minimum values in set
print("\n\nQuestion - 4")
list_a = list(a) # converting to list
list_a.sort() # sorting a list
print("min value : ",list_a[0]) # min value = at index 0
print("max value : ",list_a[len(list_a)-1]) # max value  = at last index = (length-1) index

# 5) finding most common elements from list,tuple,dictionary and their count...
print("\n\nQuestion - 5")
# in list we have
