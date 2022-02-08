
listA = [1, 2, 3, 4, 5]
result = map(lambda x: x*x, listA)
print(list(result))


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def div(a, b):
    return a/b


def mul(a, b):
    return a*b


num_list = [1, 2, 3, 4, 5]
basic_arithmetic = list(map(lambda x: [add(x, x), sub(x, x), div(x, x), mul(x, x)], num_list))
print(basic_arithmetic)