# this is solution of practical no.3 by 20CE054-Henil Rakeshbhai Mistry
"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.


Input Format:
The first line contains the n, the participants who have participated and got some score.
The second line contains an array A[]  of n integers each separated by a space.

Output Format:
Print the runner-up score.

Sample Input:
5
2 3 6 6 5

Sample Output:
5

Explanation: Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up
score.
"""

# solution ....

# phase:1 - taking inputs from the user... =============================================================================
n = int(input("Enter the total number of participants : "))  # n = total participant...
listOfScore = []  # list of all participant's score...
for i in range(n):
    listOfScore.append(int(input()))

# phase:2 - actual solution... =========================================================================================

# making set of unique score, because it is possible that two participants can have same score
setOfScores = set(listOfScore)
uniqueScoreList = list(setOfScores)  # making the list out of it for sorting...
uniqueScoreList.sort(reverse=True)  # sorting in reverse/descending ...
runnerUp = uniqueScoreList[1]  # so that the 2nd position's point/score is the runner ups score...

# phase:3 - printing the answer... =====================================================================================
print("Runner ups score is : ", runnerUp)
