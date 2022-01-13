# conditional statements are here...
"""
we don't need to do condition in parentheses...
we can just do the condition and then use ":" colon...that's it...
even we don't need to write body of statement in {}....

we can make else if...just by writing elif in python....
example:

if <condition-1> :
    <body...to be executed ...
    ....
    ....>
elif <condition-2> :
    <body...to be executed ...
    ....
    ....>
...
...
...
else:
    <default condition body...
    ....
    ....>
"""

# declared integer variable...
a = 40

# if-elif-else ladder in python...
print("Result from if-elif-else ladder.")
if a > 50:
    print("The value is greater than 50.")
elif a > 40:
    print("The value is greater than 40.")
elif a > 30:
    print("The value is greater than 30.")
else:
    print("The value is less than 30.")

# nesting of if-elif-else...
print("\n\nResult from nesting of if-elif-else ladder.")
if a >= 50:
    if a > 55:
        print("The value is in range of 55-infinite.")
    elif a > 51:
        print("The value is in range of 51-55.")
    else:
        print("The value is 50.")
elif a >= 40:
    if a > 45:
        print("The value is in range of 45-49.")
    elif a > 40:
        print("The value is in range of 41-45.")
    else:
        print("The value is 40.")
else:
    print("The value is in range of (-infinite)-39.")

# simple if-else ladder that checks the eligibility of user to vote...
print("\n\nsimple if-else ladder that checks the eligibility of user to vote...")
age_of_user = 15
print("User age : ", age_of_user)
if age_of_user >= 18:
    print("User is eligible for voting.")
else:
    print("User is not eligible for voting.")

# of course if we are using conditional statements the we must know about operators...
"""
The operators in python...
python arithmetic operators...
    --> +, -, *, /, % (usual once)
    --> ** exponential operator
    --> // floor division operator

python comparison operators...
    --> ==, !=, >, <, >=, <= (usual once)

python logical operators...
    --> and (performs and operation --> returns true if both conditions are true) same as "&&"
    like wise...
    --> or same as "||"
    --> not same as "!="

python identity operators...
    --> is (returns true if both variables are same)
    --> is not (returns true if both variables are not same)
    
python membership operators...
    --> in (returns true if specified value is in given sequence)
    --> not in (returns true if specified value is not in given sequence)

"""