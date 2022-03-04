"""
"Association"
"Aggregation"
"Composition"

(_*) 5 pillars in Object-Oriented Programming in Python...
-> Encapsulation
    --> It is a mechanism of restricting direct access to the data of class to outer user.
-> Data hiding
    --> without knowing the internal commands,tasks we are allowing others to access it
-> Inheritance
    --> It is a mechanism of basing some already existing class upon another class which leads to inhering all the
        attributes and methods of already existing class into new one...
-> Polymorphism
    --> two or more instances of similar entity,function or set of instructions can be constructed
-> Division of responsibility
    --> the re-usability and the division of similar functions,tasks can be done to ease the maintenance in future

(_*) Classes
    -> It is a group of functions, which relates to each other.
    -> It provides a means of building data and functionality together.
    -> Contrast from module, the classes are way simpler and relative combination of group of functionality.

(_*) User friendly notes...
    -> Classes in python are created by key-word 'Class'
    -> Attributes are the data or variables of class
    -> We can access attributes or methods of the cass by creating instance of a class which is known as object of type
        class and for accessing, we need to use '.' operator...
"""


class Person:
    name = "Default_Name"
    __age = 18
    __gender = "Male_Default"

    # constructor/init. method...
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.__gender = gender

    # getter and setters...
    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender


if __name__ == "__main__":
    p1 = Person("Henil Mistry", 18, "Male")
    print("Before set, Age : ", p1.getAge())
    p1.setAge(25)
    print("Name : ", p1.name)
    print("Age : ", p1.getAge())
