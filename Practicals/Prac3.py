# this is solution of practical no.3 by 20CE054-Henil Rakeshbhai Mistry
"""
Mr. Anand is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting K of  members per group where  K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group. Mr. Anand has an unordered list of
randomly arranged room entries. The list consists of the room numbers for all the tourists. The room numbers will
appear K times per group except for the Captain's room. Mr. Anand needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you. You only know the value of K
 and the room number list.

Input Format:
The first line consists of an integer, K , the size of each group.
The second line contains the unordered elements of the room number list.

Constraints:
1< K<1000

Output Format:
Output the Captain's room number.

Sample Input:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

Sample Output:
8

Explanation: The list of room numbers contains 31 elements. Since K is 5, there must be 6 groups of families.
In the given list, all the numbers repeat 5 times except for room number 8.
Hence,  8 is the Captain's room number.
"""

# solution...

# phase-1 : taking inputs from the user... ============================================================================
K = int(input("Enter the group size of tourist : "))  # k = group size...
listOfAllocatedRooms = list(input("Enter the room allocation list : "))  # list of allocated room to each tourist...

# phase-2 : actual solution... =========================================================================================


def findCaptainsRoom(listOfAllocation):  # made this function for user's ease...
    setOfRooms = set(listOfAllocation)
    return findCaptainsRoom(setOfRooms, listOfAllocation)


def findCaptainsRoom(setOfRooms, listOfAllocation):  # made this function...
    for roomNo in setOfRooms:  # looping through each room allocated...
        if listOfAllocation.count(roomNo) == 1:  # if room allocated only once is appeared in list...
            return roomNo  # that is the captain's room because he is allocated separated room
        else:
            continue


setOfAllocatedRooms = set(listOfAllocatedRooms)
captainsRoom = findCaptainsRoom(setOfAllocatedRooms, listOfAllocatedRooms)

# phase-3 : printing answer... =========================================================================================
print("Captains Room No : ", captainsRoom)
