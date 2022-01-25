"""
-> keyword based arguments
-> non-keyword based arguments
-> Lambda functions
-> self-invoking lambda function
-> higher order functions
-> Closure
    => accessing the function which is not in our scope; or accessing the function which is nested in some other
    function...
    => one kind of encapsulation
-> Decorator

"""

# passing variable number of arguments in function in python ===========================================================
"""
We often doesn't sure about the exact number of arguments that will be passed in function, designed by us...
-> in such scenarios we can use special character "*", alerting to compiler that here the arguments will be in variable
numbers each time of call to this function...
    
    => usually we can design two types of function....
        -> keyword based...
            ex. def function(fname = "henil", lname = "mistry"):
                    <function_body>
        -> non-keyword based...
            ex. def function(a, b):
       
                    return a + b
    => we can use "*" operator to be able to make a function which accepts both, a keyword based variable arguments
        and non-keyword based variable arguments....
        ex. def function(**args)
                <function_body>
            will be able to take keyword based variable arguments...
        ex. def function(*args)
                <function_body>
            will be able to take non-keyword based variable arguments...
    
    => both type are mentioned below...
    
"""


# function, which is able to take non-keyword based variable number of arguments...
def addition_variable(*args):
    ans = 0
    for x in args:
        ans += x
    return ans


# function, which is able to take keyword based variable number of arguments...
def person_info_variable(**args):
    print("The person information, which is retrieved : ")
    for info, value in args.items():
        print(info, " : ", value)


# lambda function ======================================================================================================
"""
This is anonymous functions in python...
which can have multiple number of argument but can only have one expression...

-> the self calling lambda function is demonstrated in __main__ 
"""

# lambda function which double the value passed...
doubler = lambda a: a * 2

# closure and decorator ================================================================================================
"""
Decoration is a design pattern that allows you to modify the behavior of a function. A decorator is a function that 
takes in a function and returns an augmented copy of that function.

When writing closures and decorators, you must keep the scope of each function in mind. In Python, functions define 
scope. Closures have access to the scope of the function that returns them; the decorator’s scope
"""


def my_decorator(func):
    def closure():
        print("Before function call")
        func()
        print("After function call")

    return closure


def say_hello():
    print("Hello World!")


# another example of it...
def my_modifier_aka_decorator(n):
    # closure...
    modify = lambda a: a * n
    # returning a closure...
    return modify


# the concept of higher-order function is here =========================================================================
# defining a square function, it will return the square of the given number...
def square(x):
    return x * x


# defining a cube function, it will return the cube of the given number...
def cube(x):
    return x * x * x


# defining higher order function, it will call either above function; based on argument is passed...
def higher_order(func, arg):
    answer = func(arg)
    return answer


if __name__ == "__main__":
    # variable number of arguments in function =========================================================================
    print("variable number of arguments in function : ")
    print("addition_variable(1, 2, 3, 10, 15, 45, 50) : ", addition_variable(1, 2, 3, 10, 15, 45, 50))
    print("addition_variable(1, 2, 3, 10, 15, 45) : ", addition_variable(1, 2, 3, 10, 15, 45))
    print("calling person_info_variable(firstName='henil', lastName='Mistry', age=20) : ")
    person_info_variable(firstName='henil', lastName='Mistry', age=20)
    print("calling person_info_variable(firstName='henil', lastName='Mistry', age=20, email='henil@test.com') : ")
    person_info_variable(firstName='henil', lastName='Mistry', age=20, email="henil@test.com")

    # lambda function ==================================================================================================
    print("\n\nlambda function : ")
    print("calling lambda function doubler(5) : ", doubler(5))  # calling lambda function....

    # self calling lambda function...
    print("Self calling lambda function (lambda a: a*3)(5) : ", (lambda a: a * 3)(5))

    # closure and decorators in python =================================================================================
    print("\n\nclosure and decorators in python : ")
    hello = my_decorator(say_hello)
    print("after hello = my_decorator(say_hello) : calling hello()")
    hello()

    myDoubler = my_modifier_aka_decorator(2)
    myTripler = my_modifier_aka_decorator(3)
    print("""
    after these two lines...
        myDoubler = my_modifier_aka_decorator(2)
        myTripler = my_modifier_aka_decorator(3)
    i can use....
        myDoubler(<value>) : it will return 2*<value>
        like wise for myTripler...
    """)
    print("myDoubler(10) : ", myDoubler(10), "myTripler(10) : ",  myTripler(10))

    # higher order functions ===========================================================================================
    print("\n\nhigher order functions : ")
    function_name = input("Enter the operation : ")
    argument = int(input("Enter the value/argument : "))
    if function_name.lower() == "square":
        result = higher_order(square, argument)
        print(result)
    elif function_name.lower() == "cube":
        result = higher_order(cube, argument)
        print(result)
    else:
        print("Some Error Occurred!")
