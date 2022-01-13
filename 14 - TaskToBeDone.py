# person dictionary is created over here...
CE054 = {
    "FirstName": "Henil",
    "LastName": "Mistry",
    "Address": {
        "StreetName": "Golwad Street",
        "StrretNo": 94,
        "Pincode": 395004
    },
    "Skills": ["C", "C++", "Java", "Javascript", "HTML", "CSS", "PHP", "Unity3D"]
}

CE064 = {
    "FirstName": "Harshil",
    "LastName": "Padsala",
    "Address": {
        "StreetName": "varachha",
        "StrretNo": 64,
        "Pincode": 395064
    },
    "Skills": ["Python", "Javascript", "HTML", "CSS", "NodeJS"]
}

CE048 = {
    "FirstName": "Maharshil",
    "LastName": "Limbachiya",
    "Address": {
        "StreetName": "Anand",
        "StrretNo": 48,
        "Pincode": 395048
    },
    "Skills": ["C++", "Javascript", "HTML", "CSS", "NodeJS", "React"]
}

CE069 = {
    "FirstName": "Dev",
    "LastName": "Nakum",
    "Address": {
        "StreetName": "varachha",
        "StrretNo": 69,
        "Pincode": 395069
    },
    "Skills": ["MySQL", "Javascript", "HTML", "CSS", "NodeJS", "MongoDB", "Android Studio"]
}

CE056 = {
    "FirstName": "Pratham",
    "LastName": "Modi",
    "Address": {
        "StreetName": "Dabholi",
        "StrretNo": 56,
        "Pincode": 395056
    },
    "Skills": ["Javascript", "HTML", "CSS", "NodeJS", "React", "MongoDB"]
}

# creator of this dictionary is, Henil Rakeshbhai Mistry : 20CE054
Batch_C1 = {
    "20CE054": CE054,
    "20CE048": CE048,
    "20CE056": CE056,
    "20CE069": CE069,
    "20CE064": CE064
}

# ----------------------------------------------------------------------------------------------------------------------
# task 1 --> if person has "skill" key then print middle key...
print("\n\nTASK-1")
"""
i have taken loop in dictionary Batch_C1 to loop through all keys...
which is composed of dictionaries so...again looped through in that..
if "skill" key is encountered then...
    --> found the length of that list...
    --> and middleValue is (0+length)/2...if skills are odd
    else middleValue is (0+length)/2 - 1 and (0+length)/2 ...
"""
for values in Batch_C1.values():  # looping in main dict. ...
    for keys in values.keys():  # looping in person's keys...
        if keys == "Skills":  # if skills are found...
            if type(values.get(keys)) == list:  # if skills are listed as list...
                length = len(values.get(keys))  # then find length of list...
                if length % 2 == 0:  # if person has even numbers of skills
                    print(values.get("FirstName"), "'s middle skills are : ", values.get(keys)[int(length / 2) - 1],
                          values.get(keys)[int(length / 2)])
                else:  # if person has odd number of skills
                    print(values.get("FirstName"), "'s middle skill is : ", values.get(keys)[int(length / 2)])

# ----------------------------------------------------------------------------------------------------------------------
# task 2 --> if person has "skill" key then check whether it contains "python" or not?
print("\n\nTASK-2")
"""
i have taken loop in Batch_C1 dictionary to loop through all person...
if they have key "skills"
    then we can find list of "skills"
        and using count() function we can find "python"
which is demonstrated below...
"""
for values in Batch_C1.values():
    for keys in values.keys():
        if keys == "Skills":
            if values.get(keys).count("Python") > 0:
                print(values.get("FirstName") + " contains python as a skill.")
            else:
                print(values.get("FirstName") + " does not contains python as a skill.")

# ----------------------------------------------------------------------------------------------------------------------
# task 3 --> choose or print appropriate title for person according to skills they have
"""
for example:
    --> if person have skills of JS, React
        --> then title should be "Front-end developer"
    --> else if person have skills of Python, MongoDB, MySQL
        --> then title should be "back-end developer"
    --> else if person have skills of JS, React, MongoDB
        --> then title should be "full-stack developer"
    --> else
        --> title should be "unknown"
        
i have created dictionary for titles in which each title contains
certain skills required to achieve so by comparing skills with this dictionary of
title we can find best match for any person...
"""
print("\n\nTASK-3")
for person in Batch_C1.values():
    for keys in person.keys():
        if keys == "Skills":
            Skills = person.get(keys)
            if Skills.count("Android Studio") > 0:
                print(person.get("FirstName"), " is Android developer.")
            elif Skills.count("Unity3D") > 0:
                print(person.get("FirstName"), " is Game developer.")
            elif Skills.count("Javascript") > 0 or Skills.count("React") > 0:
                if Skills.count("MongoDB") > 0 or Skills.count("MySQL") > 0 or Skills.count("PHP") > 0:
                    print(person.get("FirstName"), "is full-stack developer.")
                else:
                    print(person.get("FirstName"), "is front-end developer.")
            elif Skills.count("MongoDB") > 0 or Skills.count("MySQL") > 0 or Skills.count("PHP") > 0:
                print(person.get("FirstName"), "is back-end developer.")
            else:
                print("Unknown-title!")

# ----------------------------------------------------------------------------------------------------------------------
# task 4 --> iterate from 0 to 100 and find sum of all even and all odd
print("\n\nTASK-4")
sumO = 0
sumE = 0
for i in range(0, 101):  # from 0-100
    if i % 2 == 0:  # i is even...
        sumE += i
    else:  # i is odd...
        sumO += i
print("Sum of all even in range 0-100 is : ", sumE)
print("Sum of all odd in range 0-100 is : ", sumO)

# ----------------------------------------------------------------------------------------------------------------------
# task 5 --> check that all items in list are unique or not?
print("\n\nTASK-5")
"""
we can take help of definition of list and set...
set is collection or non-repetitive values...
hence if we convert list into set which is having all distinct element from each other
then list size = set size
"""

# declaring two lists...
listA = [1, 2, 3, 4, 5]  # list with all distinct elements...
listB = ["Henil", "Rakeshbhai", "Mistry", "Henil"]  # list with repetitive elements...


# function to handle operation...
def validateDistinctness(givenList):
    if len(set(givenList)) == len(givenList):
        return "List is not having any duplicate elements, all elements in list are distinct from each other."
    else:
        return "List is having some duplicate elements."


print("listA : ", listA)
print("listB : ", listB)
print("validateDistinctness(listA) : ", validateDistinctness(listA))
print("validateDistinctness(listB) : ", validateDistinctness(listB))

# ----------------------------------------------------------------------------------------------------------------------
# task 6 --> check that all items in list have same datatype...
print("\n\nTASK-6")
"""
if list is having all elements of same datatype...
then we can loop through each element...and compare the datatype with first elements
"""


def validateSametype(givenList):
    if type(givenList) is not list:
        return None
    else:
        validation = True
        for element in givenList:
            if type(givenList[0]) is not type(element):
                validation = False
                break
            else:
                continue
        return validation


listC = [1, "henil", 2]
print("listC : ", listC)

print("validation of listA using validateSametype(listA) : ", validateSametype(listA))
print("validation of listC using validateSametype(listC) : ", validateSametype(listC))

# ----------------------------------------------------------------------------------------------------------------------
# task 7 --> check that variable name is valid in python or not?
print("\n\nTASK-7")
"""
python variable name must not be any keyword in python
and also it must follows general variables rules...
that we need to follow while declaring variables...
and for that...

we can take help of two functions...
 --> <str>.isidentifier() : returns true if it is valid identifier
"""

def validateVarName(givenName):
    if type(givenName) is not str:
        return None
    else:
        if givenName.isidentifier():
            return "Yes"
        else:
            return "No"


print("is 'Henil' is valid variable name : ", validateVarName('Henil'))
print("is '1Henil' is valid variable name : ", validateVarName('1Henil'))
print("is 'Hen-il' is valid variable name : ", validateVarName('Hen-il'))
print("is 'Hen_il' is valid variable name : ", validateVarName('Hen_il'))
