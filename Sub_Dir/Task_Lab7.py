"""
we need to implement the following code, using lambda function...

def fruit_start_with_A(start):
    return start[0] == "A"


fruit_names = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(fruit_start_with_A, fruit_names)
print(list(map_object))
print(list(map(str.upper, fruit_names)))

"""

# fruit names are here...
fruit_names = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_obj = map(lambda x: x[0] == "A", fruit_names)
print(list(map_obj))
# print(fruit_names_start_with_A)
