# this is solution of task - 2 of lab5
# by : 20CE054 - Henil Mistry

if __name__ == "__main__":
    # subtask - 1 : Flattening the list which contains nested list into one-dimension...using comprehensions...
    # more details about comprehensions is listed in '20 - comprehensions.py' file.
    listA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    listB = [[1, 2], [3, 4, 5, 6], [7], [8, 9]]
    # this task can be done using loops also, but it requires more time, space, lines of codes
    # while working with comprehensions doesn't require all that...

    # this is list comprehensions...
    print("Subtask-1 : Flattening the list using list comprehensions...")
    print("listA : ", listA)
    print("listB : ", listB)
    flatten_list = [x for subList in listA for x in subList]
    print("after flatten_list = [x for subList in listA for x in subList] : ")
    print("flatten_list : ", flatten_list)
    flatten_list = [x for x in listB for x in x]
    print("after flatten_list = [x for x in listB for x in x] : ")
    print("flatten_list : ", flatten_list)

    # end of subtask-1 =================================================================================================

    # subtask - 2 : we need to create a list of tuples as follows...
    """
        givenListOfTuples = [(0, 1, 0, 0, 0, 0, 0),
                             (1, 1, 1, 1, 1, 1, 1),
                             (2, 1, 2, 4, 8, 16, 32),
                             ...
                             ...
                             (10, 1, 10, 100, 1000, 10000, 100000)]
        
        if we observe carefully there exist 7 elements in each tuple...
        starting from number and followed by result of power of number from 0-5
        so it is like this...
        (number, number^0, number^1, number^2, number^3, number^4, number^5)
    """
    print("\n\nSubtask-2 : creating a list of tuple using list comprehension...")
    requiredList = [(n, pow(n, 0), pow(n, 1), pow(n, 2), pow(n, 3), pow(n, 4), pow(n, 5)) for n in range(11)]
    print("after requiredList = [(n, pow(n, 0), pow(n, 1), pow(n, 2), pow(n, 3), pow(n, 4), pow(n, 5)) for n in "
          "range(11)] : ")
    print("requiredList : ", requiredList)

    # end of subtask-2 =================================================================================================

    # subtask - 3 : flattening the list to get desired output...
    print("\n\nSubtask - 3 : flattening the list to get desired output...")
    listC = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    print("listC : ", listC)
    moderate_flat_list = [x for subList in listC for x in subList]
    print("after moderate_flat_list = [x for subList in listC for x in subList] : ")
    print("moderate_flat_list : ", moderate_flat_list)
    flat_list = [[str.upper(a), str.upper(a[:3]), str.upper(b)] for (a, b) in moderate_flat_list]
    print("after flat_list = [[str.upper(a), str.upper(a[:3]), str.upper(b)] for (a, b) in moderate_flat_list] : ")
    print("flat_list : ", flat_list)

    # end of task - 3 ==================================================================================================

    # subtask - 4 : flattening the list to get list of dictionary...
    print("\n\nSubtask - 4 : flattening the list to get list of dictionary...")
    listD = [[('India', 'Delhi')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
    desiredFlatList = [{'country': f'{a}', 'city': f'{b}'} for [(a, b)] in listD]
    print("listD : ", listD)
    print("after desiredFlatList = [{'country': f'{a}', 'city': f'{b}'} for [(a, b)] in listD] : ")
    print("desiredFlatList : ", desiredFlatList)

    # end of task - 4 ==================================================================================================

    # subtask - 5 : change the list of list to get list of concatenated strings
    print("\n\nSubtask - 5 : change the list of list to get list of concatenated strings...")
    listE = [[('Mistry', 'Henil')], [('Bhargav', 'Bakraniya')], [('Alkaben', 'Mistry')], [('Millie', 'Browne')]]
    result = [f'{a} {b}' for [(a, b)] in listE]
    print("result : ", result)
