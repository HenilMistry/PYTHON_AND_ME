"""
Student: Henil R. Mistry
ID: 20CE054
GitHubLink: https://github.com/HenilMistry/PythonAndMe
"""

"""
Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same
frequency of each character. If there are odd number of characters in the string, we ignore the middle character and
check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with
same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome.
The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you
need to tell if it is a lapindrome.

Input:
6
gaga
abcde
rotor
xyzxy
abbaab
ababc

Output:
YES
NO
YES
YES
NO
NO
"""

# taking inputs for total words...
totalWords = int(input())

# making dictionary that will keep track of, whether the string is lpalindrom or not?
lpalindromDict = {}

# running for loop for total words to be input...
for i in range(totalWords):
    word = input()
    if word == word[::-1]:  # the word is l-palindrom...
        lpalindromDict.update({word: "YES"})
    else:
        # separating string in two parts...
        leftPart = word[:int(len(word)/2)]
        rightPart = ""
        if len(word) % 2 == 0:
            rightPart = word[int(len(word)/2):]
        else:  # skipping middle character...
            rightPart = word[int(len(word)/2)+1:]

        if leftPart == rightPart:  # if two part are same...
            lpalindromDict.update({word: "YES"})
        elif leftPart == rightPart[::-1]:  # if in two parts, character frequency is matching...
            lpalindromDict.update({word: "YES"})
        else:  # this word is not l-palindrom...
            lpalindromDict.update({word: "NO"})

# printing answer...
for result in list(lpalindromDict.values()):
    print(result)
