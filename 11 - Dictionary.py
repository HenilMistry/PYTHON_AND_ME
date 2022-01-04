# Dictionary, in simple words the meaning of different terms
# Dictionary is collection of key and value pair type data
# syntax is as shown below...

Dictionary = {'a': 5, 'b': 10, 'c': 25, "Bro": "Shane"}
a = {1: "Henil", 2: "Rakeshbhai", 3: "Mistry", "Bro": "Krish"}

print("Dictionary : ", Dictionary)
print("a[1] : ", a[1])

"""
some properties of dictionary to be known ...

1) it is unordered
2) it is mutable
3) it is indexed
4) duplicate values of keys cannot be there
--> if we try to enter duplicated keys, it will simply replace the previous data which was stored
as key value pair with that key...

some methods of dictionary ...
keys() ... returns the keys of dictionary...return type is 'dict_keys'
values() ... returns the values of dictionary...return type is 'dict_values'
list() ... return the 'dict_list' of key and value pairs of dictionary # use of this can be understood with loops...
update() ... updates the current dictionary
get(<key>) ... returns the <value> in current dictionary with <key> passed in argument

"""

# keys() method ...
print("\n\nkeys() method...")
print("a.keys() : ", a.keys())
print("list(a.keys()) : ", list(a.keys()))

# values() method ...
print("\n\nvalues() method...")
print("Dictionary.values() : ",Dictionary.values())
print("list(Dictionary.values()) : ",list(Dictionary.values()))

# update() method ...
print("\n\nupdate() method...")
Dictionary.update({"Heal" : "Brother"})
print("After 'Dictionary.update({'Heal','Brother'})' : ",Dictionary)
Relations = {
    "Mother" : "Alkaben",
    "Father" : "Rakeshbhai"
}
Dictionary.update(Relations)
print("After Dictionary.update(Relations) : ",Dictionary)

# get() method ...
print("\n\nget() method...")
print("Dictionary.get('Bro') : ",Dictionary.get('Bro'))
print("Dictionary['Bro'] : ",Dictionary['Bro'])
# the difference between the get() method and 'Dictionary[<key>]' ...
print("Dictionary.get('Apple') : ",Dictionary.get("Apple")) # this will return none
print("Dictionary['Apple'] : will throw error while get() method doesn't ...")
# print("Dictionary['Apple'] : ",Dictionary["Apple"]) # this will throw error

# creating dictionaries...
Charotar_Inst_CSPIT = {
    'Departments': [{
        'Name': 'CE',
        'Batches': {
            'C1': [1, 2, 3, 4, 5],
            'C2': [6, 7, 8, 9, 10]
        }
    }, 'ME', 'IT', 'CSE']
}
Charotar_Inst_DEPSTAR = {

}
Charotar_Institute = {
    'CSPIT': Charotar_Inst_CSPIT,
    'DEPSTAR': Charotar_Inst_DEPSTAR
}
Universities = {
    'Charotar University': Charotar_Institute
}
print(Universities)

# pop() and popItem() ....
print("\n\npop() and popitem() methods ...")
Dict = {
    'Mother': 'Alkaben',
    'Father': 'Rakeshbhai'
}
print("Dictionary : ", Dict)
ax = Dict.pop("Mother")
print("after a = Dictionary.pop('Mother') a : ", ax)
# Dictionary.update({'Mother': 'Alkaben'})
bx = Dict.popitem()
print("after bx = Dict.popitem() bx : ", bx)

# fromkeys() method...
print("\n\nfromkeys() method...")
Dict_XYZ = {}
Dict_XYZ = Dict_XYZ.fromkeys(list(Dictionary.keys()), ["myKeys"])
print(Dict_XYZ)

# setdefault(<key>,<value>) method...
# if key exist then doesn't do anything...
# if key doesn't exist then add a key...
x = Dictionary.setdefault("Mother", "Alkaben")
print(x)
x = Dictionary.setdefault("Bros ",["heal","het","hardik"])
print(x)

# assignment 2 was solved from here ===================================================================================
# 1) checking whether a key is existing in dictionary or not
print("\n\nQuestion - 1")
ListKeys = list(Dictionary.keys()) # created a list of keys from dictionary
# as a property of key that dictionary cannot contain duplicate keys so...
print("ListKeys in Dictionary : ",ListKeys)
print("If result is 1 then key exist in dictionary or else not! --> property of key in dictionary!")
print("result of ListKeys.count('h') is : ",ListKeys.count('h')) # if the key is exist the o/p will be 1 or else it will be 0...


# 2) merging two dictionaries
print("\n\nQuestion - 2")
b = {

}
print("before any updation b : ",b)
b.update(Dictionary)
b.update(a)
print("after b.update(Dictionary) and b.update(a) : ",b)

# 3) sum all elements in dictionary
print("\n\nQuestion - 3")
sDict = {
    'a' : 100,
    'b' : 10,
    'c' : 55,
    # 'd' : "henil" adding this string value will leads error...
}
print("sDict : ",sDict)
val = sDict.values()
sum = sum(val)
print("values : ",val," sum : ",sum)

# 4) add a key to dictionary
print("\n\nQuestion - 4")
print("before adding operation a : ",a)
a.update({ 4 : "Prajapati"})
print("after a.update({ 4 : 'Prajapati'}) a : ",a)

# 5) concating dictionaries to create a new one
print("\n\nQuestion - 5")
x = {
    'a' : 'letter-A',
    'b' : 'section-B'
}
y = {
    "Pankha" : "Fan",
    "Thali" : "Dish"
}
z = {
    10 : 20,
    20 : 30
}
resultDict = {}
print("before concating result : ",resultDict)
resultDict.update(x)
print("after resultDict.update(x) : ",resultDict)
resultDict.update(y)
print("after resultDict.update(y) : ",resultDict)
resultDict.update(z)
print("after resultDict.update(z) : ",resultDict)
