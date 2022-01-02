# this is single line string...
String = "This is single line!"
# String = 'Python's Libraries!' this is invalid...
# String = "Python's Libraries!" this is valid...
print(String)

# Multiline string...===============================================================================================================
String = """Johhy!...Johhny!....
Yes Papa.
Eating Sugar?....
No Papa,
Open Your Mouth.
ha ha ha.....!"""
print(String)
# Multiline string...with other way...
String = '''This is also a multiline,
in python. All the work is easy with python,
you just need to practice and sharpen up your
knowledge time to time.'''
print(String)

# concatination of string ==========================================================================================================
FirstName = "Henil"
MiddleName = "Rakeshbhai"
LastName = "Mistry"
FullName = FirstName+" "+MiddleName+" "+LastName
print(FullName)

# string length using in-built function =====================================================================================
print("\n\nLength of First Name : ",len(FirstName))
print("Length of Full Name : ",len(FullName))

# unpacking characters ===========================================================================================================
a,b,c,d,e = FirstName
print("\n\nAfter unpacking with 'a,b,c,d,e = FirstName'")
print("a : ",a,"\nb : ",b,"\nc : ",c,"\nd : ",d,"\ne : ",e)
f,g,*h = MiddleName
print("After unpacking with 'f,g,*h = MiddleName'")
print("f : ",f,"\ng : ",g,"\nh : ",h)
i,*j,k = LastName
print("After unpacking with 'i,*j,k = LastName'")
print("i : ",i,"\nj : ",j,"\nk : ",k)

# indexing of string in python ================================================================================================
# normal indexing which we use in other languages.....
print("\n\nNormal indexing in python")
print("FirstName[0] : ",FirstName[0])
print("MiddleName[1] : ",MiddleName[1])
print("LastName[2] : ",LastName[2])
print("FullName[20] : ",FullName[20])

# if we want that we need to print from r.h.s. the  we can use negative index...
print("\n\nNegative indexing in python")
print("FirstName[-1] : ",FirstName[-1])
print("MiddleName[-2] : ",MiddleName[-2])
print("LastName[-3] : ",LastName[-3])
print("FullName[-20] : ",FullName[-20])

# slicing of string in python ================================================================================================
print("\n\nSlicing of string in python")
print("FirstName[1:4] : ",FirstName[1:4])
print("FullName[6:10] : ",FullName[6:16])
# if we leave lower bound as empty then it will consie it 0
print("FullName[:6] : ",FullName[:6])
# if we leave upper bound as empty then it will consider it as length of that string
print("FullName[6:] : ",FullName[6:])
# we can also give third argument in that square brackets as steps to skip each time after printing index....
print("FullName[::2] : ",FullName[::2])
print("FullName[::3] : ",FullName[::3])
print("FullName[::4] : ",FullName[::4])

# slicing from r.h.s. ========================================================================================================
print("\n\nSlicing from r.h.s.")
print("FirstName[-1:] : ",FirstName[-1:])
print("FirstName[-2:] : ",FirstName[-2:])
print("FirstName[-3:] : ",FirstName[-3:])

# string methods in python ==========================================================================================
# capitalize() method...
print("\n\ncapitalize() method...")
Name = "henil rakeshbhai mistry"
print("Name : ",Name)
print("Name.capitalize() : ",Name.capitalize())

# count() metho...returns occurance of substring passed as argument in string....
print("\n\ncount() method...")
print("Name.count('h') : ",Name.count('h'))
print("Name.capitalize().count('h') : ",Name.capitalize().count('h'))

# endswith() method...returns true if the substring passed as argument is ending of the string...
print("\n\nendswith() method...")
print("Name.endswith('Mistry') : ",Name.endswith('Mistry'))
print("Name.capitalize().endswith('Mistry') : ",Name.capitalize().endswith("Mistry"))
print("FullName.endswith('Mistry') : ",FullName.endswith('Mistry'))
print("LastName.endswith('Mistry') : ",LastName.endswith('Mistry'))

# expandtabs() method...replaces tab character with spaces which is passed as argument in this method...
# by default it takes 8 as argument if not passed any...
print("\n\nexpandtabs() method...")
challange = "programming\tin\tpython"
print("challange.expandtabs() : ",challange.expandtabs())
print("challange.expandtabs(5) : ",challange.expandtabs(5))
# research that how it gives the spaces in place of tabs....

# find() method...find the first occurance of substring passed as argument in string...
print("\n\nfind() method...")
print("Name.find('Mistry') : ",Name.find('Mistry'))
print("Name.capitalize().find('Mistry') : ",Name.capitalize().find('Mistry'))
print("FullName.find('Mistry') : ",FullName.find('Mistry'))
print("FullName[FullName.find('Rakeshbhai'):FullName.find('Mistry')] : ",FullName[FullName.find('Rakeshbhai'):FullName.find('Mistry')])
print("FullName[FullName.find('Rakeshbhai'):FullName.find('Mistry')].find('rakeshbhai') : ",FullName[FullName.find('Rakeshbhai'):FullName.find('Mistry')].find('rakeshbhai'))

# casefold vs lowercase function...
String = "Henil_ß"
print("\n\nDifferenece between casefold() and lowercase() method...")
print("String : ",String)
print("String.lower() = ",String.lower())
print("String.casefold() = ",String.casefold())

# slice and reverse function...
print("\n\nReversing a string using a spliting concept...")
String = "I am henil rakeshbhai mistry."
print("String : ",String)
print("String[::-1] : ",String[::-1]) # reverse string...

# formatting a string or dynamically filling holes which are there in our string...
print("\n\nForamatting a string...or...dynamically insering a values in holes...")
Sentence = "My name is {}. I am a {} and i am {} years old."
Name = "Henil Mistry"
Profession = "Student"
Age = "19"
print("Sentence.format(Name,Profession,Age) : ",Sentence.format(Name,Profession,Age))

# swapcase, join, replace, strip, split, startswith.....