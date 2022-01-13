# functions are set of statements that needs to be called repetitively in program
# whenever its needed

# the main difference between loops and functions is that
# the block of statements which needs to be called repetitively with certain condition is true
# then we use loop
# the block of statements which needs to be called repetitively in program but at different-different locations
# then we use functions to group all that statements and call a function
# whenever it is needed...

"""
The function is a group of statements which performs specific task.
The function helps to reduce the lines of code to be written.

In Python, we use "def" keyword to define a function
 for example:
    def <function_name>(<arguments_one_or_many>):
        <body_of_function......
        ...
        ...
        group of statements, performing a task
        ...
        ...>

"""

# function with default parameter values
print("Function with default parameters : ")
"""
giving the default parameter values will help to reduce error to be thrown if
some unexpected things has happened..
for example :
    in this greeting function, the user forgot to mention greeting message
    or the user forgot to give the name of the person whom he/she wants to greet!

--> In such cases, the default parameter will be taken into consideration...
"""


def GreetTo(whom="Henil Mistry", message="Welcome to world of python programming!"):
    return "Hello! " + str(whom) + ", " + str(message)


def Greet(whom):
    return GreetTo(whom)


# making a list of person who has attended seminar...
listOfPerson = ["Henil Mistry", "Heal Mistry", "Nidhi Bhatra", "Bhargav Bakraniya", "Bhargavi Dave", "Parth Darji"]
# greeting to all person who has attended the seminar...
for person in listOfPerson:
    print(Greet(person))

# function with variable arguments...
print("\n\nFunction with variable arguments and '*'(rest) operator :")
"""
suppose at a time of grouping the statements for making a function
if we don't know the no. of arguments that can be passed
or we don't sure at that time about the no. of arguments then
we can use variables arguments....

which can be achieved using rest "*" operator...
which is demonstrated below..
 
"""


def Add(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Mul(a, b):
    return a * b


def Div(a, b):
    return a / b


def AddAll(elements1, *restAll):
    result = 0
    result += elements1
    for x in restAll:
        result += x
    return result


def Max(element1, *restAll):
    listOfElement = list(restAll)
    listOfElement.append(element1)
    MAX = 0
    for i in range(len(listOfElement)):
        if listOfElement[i] > MAX:
            MAX = listOfElement[i]
    return MAX


print("AddAll(1, 5, 70, 54, 18, 2, 50) : ",AddAll(1, 5, 70, 54, 18, 2, 50))
print("AddAll(54, 18) : ", AddAll(54, 18))
print("Max(5, 10) : ", Max(5, 10))
print("Max(5, 18, 10) : ", Max(5, 18, 10))

# switch case demonstration
print("\n\nUsing switch case with 'match' keyword : ")


def MatchCase(case):
    match case:
        case 1:
            return Add(x, y)
        case 2:
            return Sub(x, y)
        case 3:
            return Mul(x, y)
        case 4:
            return Div(x, y)
        case _:
            return "Unknown Error!"


x = int(input("----- Enter x : "))
y = int(input("----- Enter y : "))

print("""
Enter your operation as per choice is given:
1 : for addition
2 : for subtraction
3 : for multiplication
4 : for division
Enter your choice : 
""")
UserInput = int(input())
print("Result : ", MatchCase(UserInput))
