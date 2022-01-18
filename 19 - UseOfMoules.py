import MyModule as mod  # importing whole module and renaming...
from MyModule import Addition  # importing the specific function from module...
from MyModule import Subtraction as Sub  # importing the specific function from module and renaming...
import Sub_Dir.Snake_Water_Gun_Game as game  # importing from other directory...

"""
we can import the modules by using 'import' statement as mentioned above
then the use of any functions/variables/etc. can be done using '.' dot operator...
    ex.
        MyModule.<variable_name> or
        MyModule.<function_name>(<arguments_if_any>)
        
        
if we want to rename the module on temporary bases the we can us 'as' keyword
    ex. 
        import MyModule as mod
--> this functionality can be helpful when the module name is very large, that can give burden because whenever we use
some functions/variables which is inside that module, we need to write whole name of that module...


if we want to import some specific functions or class or variables from specific module then we can use
'from' keyword...
    ex.
        from MyModule import <function_name>

"""

# we can use this to see that what is inside the module that we have imported...
print(dir(mod))
# use of function from imported module...
print(Addition(5, 5))
print(Sub(-5, 5))

# playing game once...
game.playOneRound()
