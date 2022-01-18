# this is solution of task - 1 of lab5
# by : 20CE054 - Henil Mistry

# importing the required module to do the tasks given
import random as r
import string

# subtask-1 : Call your function "shuffle_list" which takes a list as parameter and returns the shuffled list ==========
# approach that i have taken...

"""
There exist lots of ways to do this but in the task they have listed by using
--> 'Using random.shuffle()' and 
--> 'Using random.sample()' and
--> 'Without using in-built functions'

*) random.shuffle() function takes a list as a parameter and shuffle the list which is passed as an argument and modify 
the actual list...also it doesn't return anything

*) random.sample() function takes two arguments, first argument for actual list and second argument which is the size of
the list that needs to be derived from actual list but shuffled...also note that it returns the list
--> it is also need to be noted that while giving the second argument, if actual list which is passed in first argument
is n then second argument must be in range 1 to n;

*) without using in-built functions, we can use randint() function which is part of random module and it takes two
arguments first argument for starting limit and second argument for ending limit and it returns the random integer
in between starting and ending limit... by using this function and for loop we can shuffle the list...

all the ways are demonstrated below...

"""


# using in-built functions...
def shuffle_list_shuffle(listX):
    if type(listX) == list:
        r.shuffle(listX)


def shuffle_list_sample(listX, size):
    if type(listX) == list:
        shuffled_list = r.sample(listX, size)
        return shuffled_list
    else:
        return None


# without using the in-built functions...
def shuffle_list(listX):
    if type(listX) == list:  # checking the type of parameter passed!
        shuffled_list = []
        while len(listX) > 0:  # while there exist elements in the given list
            index = r.randint(0, len(listX)-1)  # select the random index...
            shuffled_list.append(listX[index])  # append that index into new list...
            listX.remove(listX[index])  # remove that index from given list...
        return shuffled_list  # if given list becomes empty then return the shuffled_list
    else:
        return None

# subtask-2 : declare a function named user_id_gen_by_user() which takes no argument but takes two input from user using
# input() and first argument = number of characters, second argument = number of ids to be generated...
# approach that i have taken...


"""
i have used random.choices() function which takes sequence for generating random everytime and in that function 
i have passed set of ascii characters and digits, we know that set is sequence and hence, imported string module for it
also it is demonstrated below...

"""


def user_id_gen_by_user():
    # taking inputs required to generate the list of random ids..
    size = int(input("Enter the size of each random id : "))
    no_of_ids = int(input("Enter the number of ids which you want to generate : "))

    # making an empty list for storing the random ids...and temporary string...
    list_of_ids = []
    temp_str = ""

    # making 'no_of_ids'...each consisting of 'size' random characters...
    for x in range(no_of_ids):
        # resetting the temporary string...
        temp_str = ""
        for y in range(size):
            # appending the random character 'size' times...
            temp_str += r.choice(string.ascii_letters + string.digits)
        # adding the random id into list...
        list_of_ids.append(temp_str)

    # returning the list of ids...
    return list_of_ids


if __name__ == "__main__":
    print("Subtask-1 : Shuffling the list using in-built functions and without using in-built functions...")
    listA = [1, 2, 3, 4, 5]
    print("listA : ", listA)
    listB = shuffle_list(listA)
    print("after listB = shuffle_list(listA) listB : ", listB)
    print("Now, with in-built functions : ")
    r.shuffle(listB)
    print("after r.shuffle(listB) listB : ", listB)
    listB = r.sample(listB, 3)
    print("after listB = r.sample(listB, 3) listB : ", listB)

    # end of subtask-1 =================================================================================================

    print("\n\nSubtask-2 : Generating random ids...")
    listX = user_id_gen_by_user()
    print("after listX = user_id_gen_by_user() listX : ", listX)

    # end of subtask-2 =================================================================================================
