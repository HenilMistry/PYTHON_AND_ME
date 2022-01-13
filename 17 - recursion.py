# function calling it-self is recursion...
# as we all know that it utilizes stack...
# many mathematical beauties can be achieved using this function...
# for example:
#   fibonacci series, factorial of higher numbers, etc.

"""
recursion of function can be done when certain base conditions for any task to be done
is known to us. for example:
    (1) in factorial of a given number:
        --> we know that the factorial of -ve numbers cannot be there
        --> 0! = 1
        --> n! = (n-1)! * n
    and by using these known facts we can use recursion and make a complicated task done easily,
    although we can use loops here but all the task don't rely on loops, and also it is needs to be
    noticed if we use loops here we cannot compute for larger numbers.

"""


# using recursion and function :
def factorial_rec(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


"""
if n = 3:
     3 * [2!]
     3 * 2 * [1]
      = 6
"""


# using loop and function :
def factorial_loop(n):
    result = 1
    for x in range(n):
        result = result * (x+1)
    return result


print("99! = ", factorial_rec(99))
