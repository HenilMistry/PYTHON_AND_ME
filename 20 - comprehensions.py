"""
Python is known for its simplicity, and it has always encouraged the developers to write code as easy as
to feel like we are reading a english language...

Python's list comprehensions is one of the best feature/example of it.
--> they are used for constructing powerful functionality in just one line of code...
--> they contain brackets containing the expressions which needs to be evaluated for each iteration...
--> also note that it is faster than loops...

"""

# consider a task...
# we want to make a list of numbers which are divisible by 3 in range of 0-99...

# completing a task...using loops...
print("Completing a task using loop : ")
listX = []
for x in range(100):
    if x % 3 == 0:
        listX.append(x)
print("listX : ", listX)

# completing a task...using comprehensions...
print("\n\nCompleting a task using list comprehensions : ")
listY = [x for x in range(100) if x % 3 == 0]
print("listY : ", listY)

"""
Nesting of comprehensions/Flattening the list...
--> nesting of comprehensions is nothing but comprehension within another one, like a nested for loop..

"""

# consider a task...
# we need to flatten the given list then...what is the approach?
listA = [[1, 2, 3], [4, 5, 6], [7, 8]]

# completing a task...using loop...
print("\n\nFlattening a list using loop : ")
listB = []
for x in listA:
    for y in x:
        listB.append(y)
print("listB : ", listB)

# completing a task...using nested comprehensions...
print("\n\nFlattening a list using nested comprehensions : ")
listC = [x for subList in listA for x in subList]
print("listC : ", listC)

"""
Dictionary comprehensions
--> the comprehensions is not limited to list...
even you can use it with dictionaries...
--> there exist certain tasks that can be very complicated but with the help of comprehensions...
it makes the job easy...
    ex. 
        task = "reverse the key,value pair in given dictionary"
        this task can be done easily with the help of comprehensions...which is demonstrated below...
"""

# making a dictionary with the help of comprehensions...
print("\n\nReversing a key,value pair in dictionary using the comprehension : ")
Dict = {Str: f"Item {Str}" for Str in range(10)}
print(Dict)
# reversing the key, value pair...
Dict1 = {value: key for key, value in Dict.items()}
print(Dict1)

"""
Set comprehensions...
--> when using {}...compiler of python automatically detects that it is set comprehensions...
but when using with key:value pair it becomes dictionary...

--> the set comprehension is shown below...

"""

print("\n\nUsing set comprehensions : ")
listOfDresses = ["Dress1", "Dress2", "Dress1", "Dress3", "Dress2", "Dress1"]
setOfDresses = {dress for dress in listOfDresses}
print("Type of setOfDresses : ", type(setOfDresses))
print("setOfDresses : ", setOfDresses)

