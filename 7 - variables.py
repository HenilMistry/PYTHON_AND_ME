"""
--> variable 
    --> it is a name given to a memory location in a program...
    --> it is a container for storing value
    --> python adapts type of a variable automatically and we do not
    need to define it explicitly...

    ex.
    a = "henil" --> variable 'a' adapts to string because
    it is having double quots...

    b = 345 --> variable 'b' adapts to integar because 
    it is not containing decimal point...

--> keywords
    --> these are reserved words in python...
    ex.
    is, as, import, True, False, and, or, etc..

    --> type python in cmd to turn on REPL and
    then type 'help("keywords")' to get the list of the keywords...

--> identifier
    --> these are the names used to identify variable, class, functions,
    etc...

--> data type
    --> it is a type of a container...
    ex.
    integer, float, string, boolean, none

"""

#this is integer data type...
a = 5

#this is floating data type...
b = 55.45

#this is string data type...
c = "henil"
#string with triple quots...
d = """hello, my name is henil.
        i am the student of charotar university."""

#this is boolean data type...
e = True

#this is none data type...
f = None

#printing data ...
print(a,b,c,d,e,f)
#printing the data type...
print(type(a),type(b),type(c),type(d),type(e),type(f))

"""
--> Rules for declaring variables...
    (1) The name of the variable can contain alphabets, numbers and 
    underscores and cannot contain wide spaces.
    (2) The name of the variable can only starts with alphabets
"""

import sys
print("Python Version : ",sys.version)