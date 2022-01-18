# copy of "18 - Snake_Water_Gun_Game.py'

# this is 1 vs. computer game called Snake, Water, Gun Game:
"""
This game is all about choosing the effective item from below
    Snake, Water, Gun
Snake is chosen by someone then only choice to beat him/her is to chose Gun
Water is chosen by someone then only choice to beat him/her is to chose Snake
Gun is chosen by someone then only choice to beat him/her is to chose Water

"""

# importing required module for this game
import random


# game() function that will declare the result of one round...
def game(com, y):
    listExpected = ['s', 'g', 'w']
    if listExpected.count(y) > 0 and listExpected.count(com) > 0:
        if com == y:
            return "This game is draw! Both had chosen same!"
        elif com == 's':
            if y == 'g':
                return "You won! Computer had chosen Snake!"
            elif y == 'w':
                return "You loose! Computer had chosen Snake!"
        elif com == 'w':
            if y == 's':
                return "You won! Computer had chosen Water!"
            elif y == 'g':
                return "You loose! Computer had chosen Water!"
        elif com == 'g':
            if y == 'w':
                return "You won! Computer had chosen Gun!"
            elif y == 's':
                return "You loose! Computer had chosen Gun!"
    else:
        return "Something went wrong! Unable to fetch game result!"


# fetch_choice() function to get the choice of computer and player...
def fetch_choices():
    # using random module, computing the choice of computer, randomly
    a = random.randint(1, 3)
    if a == 0:
        a = 's'
    elif a == 1:
        a = 'w'
    else:
        a = 'g'
    # asking for player's choice...
    print("-------------------------------------------------")
    print("Computer's Turn! Snake(s) Water(w) or Gun(g)?")
    print("-------------------------------------------------")
    b = input("Your Turn! Snake(s) Water(w) or Gun(g)? : ")
    print("=================================================")
    # returning the choices in form of list...[computer's choice, player's choice]
    return [a, b]


# playGame() function that will fetch the choices and will display the result of the round...
# this function will use above two functions...
def playGame():
    playOneRound()
    # asking for permission to play next round...
    print("=================================================")
    print("Want To Play Again : (y for 'yes' or n for 'quit') : ")
    wantAnotherRound = input()

    if wantAnotherRound == "y":
        wantAnotherRound = True
    else:
        wantAnotherRound = False

    # returning the choice...that will be handled by main loop of the game...
    return wantAnotherRound


# this function will responsible for playing one round...
def playOneRound():
    # fetching choices...
    listOfChoice = fetch_choices()
    # computing the result of this round...
    print(game(listOfChoice[0], listOfChoice[1]))


# main loop of the game is here ========================================================================================
if __name__ == "__main__":
    wantToPlay = True
    while wantToPlay:
        wantToPlay = playGame()
