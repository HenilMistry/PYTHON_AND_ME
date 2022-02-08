# this is solution of practical no.5 by 20CE054-Henil Rakeshbhai Mistry
"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
letters and vice versa. Sample Input: HackerRank.com presents "Pythonist 2".

Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""

# Solution...
# phase:1 - taking inputs from the user... =============================================================================
inputStr = input("Enter the string: ")

# phase:2 - actual solution... =========================================================================================
resultStr = inputStr.swapcase()

# phase:3 - printing the answer... =====================================================================================
print("Swap case string is: ", resultStr)
