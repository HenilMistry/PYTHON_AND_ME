"""
AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order
should correspond with the input order of appearance of the word. See the sample input/output for clarification.
Sample Input
4
bcdef
abcdefg
bcde
bcdef
Sample Output
3
2 1 1
Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds
to the output.
"""

"""
# this approach is suitable when order doesn't matter in answer...
totalWord = int(input())
mainList = []
distinctElem = set()
countList = []

# taking main list of words...this list may or may not contain duplicate words...
for i in range(totalWord):
    mainList.append(input())

# making set out of list...to get rid of duplicate words...
distinct = set(mainList)
distinctElem = list(distinct)
print(distinctElem)

# making count list...
for distinctWord in distinctElem:
    countList.append(mainList.count(distinctWord))

# printing answer...
print(len(countList))
print(countList)
"""

# this is dictionary approach...
totalElem = int(input())  # taking input about total words...

countDictionary = {}  # making a dictionary that will keep track of count of numbers for keys...

for i in range(totalElem):  # for loop to run for totalElem times...
    word = input()
    if word in countDictionary.keys():
        # print("Word already present, incrementing count!")  # just for debugging...
        countDictionary.update({word: countDictionary.get(word)+1})
        # print(countDictionary)  # just for debugging...
    else:
        # print("Word is not present, taking it in!")  # just for debugging...
        countDictionary.update({word: 1})
        # print(countDictionary)  # just for debugging...

# showing the output...
countList = list(countDictionary.values())
print(len(countList))
print(countList)
