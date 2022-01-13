# loops in python
"""
loops are to be used when we want to repeat the set of statements
if certain condition is satisfied...
for example:
    if we want to print 1-100
    then instead of writing print(1),print(2),....,print(100) lots of print statements
    we can use loop...as
    for(int i=1;i<101;i++)
    {
        print(i);
    }

but in python we don't need to use curly braces and conditions we can just do as...
    for i in range(0, 101):
        print(i)

python made the use of loops very easy and affective...

--> There are two types of loops in python
    (1) While loop (condition is checked first)
        --> syntax is as follows:
            while <condition>:
                <code that is to be executed
                until the condition is true
                .....
                .....>
    (2) For loop
        --> syntax is as follows:
            for <condition or range>:
                <code that is to be executed
                if the condition is true
                ...
                ...>

"""

# printing from 1 to 10 using while loop and applying older approach
print("Loop using old approach :")
i = 1
while i < 11:
    print(i)
    i += 1


# using new approach, printing from 1 to 10
print("\n\nLoop using new approach :")
for x in range(1, 11):
    print(x)

"""
range() function in python
    --> range function in python is used to generate ranges of numbers
    with start point, end point and also we can specify steps as follow in arguments
    
    --> range(<start_point>, <end_point>, <steps>)
    
    --> for example:
        range(8) will return 0 to 7
        range(8, 10) will return 8 and 9
        range(1, 100, 2) will return all odd numbers which are from 1 to 100
        etc.
    
    --> the best use of this range() function is with for loops because it helps us to iterate over iterables
    --> the concept of iterable is same...
    
    --> if we want to iterate over list...
    we can use...
    for i in range(len(<list_name>)):
        # do something...
"""

# printing all items in list using range...
listA = [1, 2, 5, 7, 15, 18, 54, 59]
print("\n\nPrinting all items in list using range() function :")
for i in range(len(listA)):
    print(listA[i])

# printing all items in list using "in" operator
print("\n\nPrinting all items in list using 'in' operator")
for i in listA:
    print(i)

# else with for loop
# note that the else will be executed if and only if the for loop is executed successfully
# if any abnormal termination is there using "break" it won't be executed as shown in second example
print("\n\nElse with for loop")
for i in listA:
    print(i)
else:
    print("There is no element left in list.")

# second example
print("----------SECOND EXAMPLE----------")
for x in range(100):
    print("Printing "+str(x))
    if x == 5:
        break
else:
    print("There is no element left in range.")

"""
with traditional break and continue statement
there is new "pass" statement which tends to "do nothing"

the demo is mentioned below
"""
print("\n\nPass statement : ")
for x in range(10):
    if x == 5:
        pass  # work as if continue
        # speaking that if value is 5 then skip
    else:
        print("Printing "+str(x))

print("\n\nUnique patterns in python using loops")
# pattern 1
print("Pattern 1 : sorted stairs")
for h in range(0, 5):
    print("*" * (h+1))

# pattern 2
print("\n\nPattern 2 : sorted pyramid")
for h in range(0, 5):
    print(" " * (5-h)+"* " * (h+1))

# pattern 3
print("\n\nPattern 3 : abnormal stairs")
for h in range(0, 5):
    print("*" * (5-h))

# pattern 4
print("\n\nPattern 4 : abnormal pyramid")
for h in range(0, 5):
    print(" " * h + "* " * (5 - h))

# pattern 5
print("\n\nPattern 5 : boundary")
# can replace 5 with user input...
for h in range(0, 5):
    if h == 0 or h == 5-1:
        print("* " * 5)
    else:
        print("* "+" " * 5+" *")
