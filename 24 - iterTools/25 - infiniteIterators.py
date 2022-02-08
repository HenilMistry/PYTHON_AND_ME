# the infinite iterators...
"""

1) count(start, step):
    -> it will start iteration from <start> and by taking <step> goes into infinite count mode...
    -> by default <step> = 1
"""
import itertools

print("count() function in itertools is demonstrated below...")
# it will make the infinite loop...
# for i in itertools.count(10):
#     print(i)

# to handle the program, to avoid going into infinite loop...
for i in itertools.count(11):
    if i == 21:
        break
    else:
        print(i, end=" ")

"""

2) cycle(iterable):
    -> this will print the values from container <iterable> in continuous cycle mode...
"""

print("\n\ncycle() function in itertools is demonstrated below...")
count = 1
for i in itertools.cycle("Henil"):
    if count > 15:
        break
    else:
        if count % 5 == 0 and count != 0:
            print(i, end=" ")
        else:
            print(i, end="")
        count += 1

"""

3) repeat(val, num):
    -> this function is used to repeatedly calling one value(<val> here) <num> times... 
"""
print("\n\nrepeat() function in itertools is demonstrated below...")
for i in itertools.repeat(25, 5):
    print(i, end=" ")
