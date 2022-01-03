# Dictionary, in simple words the meaning of different terms
# Dictionary is collection of key and value pair type data
# syntax is as shown below...

Dictionary = {'a' : 5,'b' : 10,'c' : 25,"Bro" : "Shane"}
a = {1 : "Henil",2 : "Rakeshbhai",3 : "Mistry","Bro" : "Krish"}

print("Dictionary : ",Dictionary)
print("a[1] : ",a[1])

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
print("a.keys() : ",a.keys())
print("list(a.keys()) : ",list(a.keys()))

# values() method ...
print("Dictionary.values() : ",Dictionary.values())
print("list(Dictionary.values()) : ",list(Dictionary.values()))

# update() method ...
Dictionary.update({"Heal" : "Brother"})
print("After 'Dictionary.update({'Heal','Brother'})' : ",Dictionary)
Relations = {
    "Mother" : "Alkaben",
    "Father" : "Rakeshbhai"
}
Dictionary.update(Relations)
print("After Dictionary.update(Relations) : ",Dictionary)

# get() method ...
print("Dictionary.get('Bro') : ",Dictionary.get('Bro'))
print("Dictionary['Bro'] : ",Dictionary['Bro'])
# the difference between the get() method and 'Dictionary[<key>]' ...
print("Dictionary.get('Apple') : ",Dictionary.get("Apple")) # this will return none
# print("Dictionary['Apple'] : ",Dictionary["Apple"]) # this will throw error

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
