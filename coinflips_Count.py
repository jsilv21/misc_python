# https://automatetheboringstuff.com/2e/chapter4/
# 100 coin flips
# Write a program to find out how often a streak of 
# six heads or a streak of six tails comes up in a randomly
# generated list of heads and tails. Your program breaks up the experiment 
# into two parts: the first part generates a list of randomly selected 'heads' 
# and 'tails' values, and the second part checks if there is a streak in it. Put
# all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of 
# the coin flips contains a streak of six heads or tails in a row. As a hint, the function call 
# random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random

def flip():
    flipValue = random.randint(1,2)
    if flipValue == 1:
        side = "Heads"
    else:
        side = "Tails"
    return side


def nStreak():
    #take inputs from player
    numFlips = int(input("Number of flips:"))
    lengthStreak = int(input("Length of streak:"))
    numRuns = 0
    heads = 0
    tails = 0
    numStreakHeads = 0
    numStreakTails = 0
    actuals = []
    #loop until hitting limit
    while numRuns != numFlips:
        side = flip()
        numRuns += 1
        if side == "Heads":
            heads += 1
            tails = 0
            #checking for streak length
            if heads >= lengthStreak:
                numStreakHeads += 1
                heads = 0 #reset counter to avoid accidentally counting streak
        if side == "Tails":
            tails += 1
            heads = 0
            #checking for streak length
            if tails >= lengthStreak:
                numStreakTails += 1
                tails = 0 #reset counter to avoid accidentally counting streak
    print('Out of %i' %numFlips + ' total flips,')
    print("Number of heads streaks:", numStreakHeads)
    print("Number of tails streaks:", numStreakTails)
    #calculate total streaks and divide by total flips, format into percentage
    #print('Chance of streak: ' + str(round((((numStreakHeads+numStreakTails)/numFlips)*100),2))+'%') 
    print('Chance of streak: %.2f' % (((numStreakHeads+numStreakTails)/numFlips)*100)+'%') 
    

nStreak()