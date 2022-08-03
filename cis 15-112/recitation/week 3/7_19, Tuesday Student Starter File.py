#####################################################
# Tuesday July 19 Student Starter File
#####################################################

import copy
import random

##########################################################
# removeRuns
# 
# Write the function removeRuns(L) which takes an int list L, and 
# destructively modifies the list so that there remains no consecutive elements 
# in L that are the same.
##########################################################

def removeRuns(L):
    prev = -1
    index = 0
    while index < len(L):
        if L[index] == prev:
            L.pop(index)
        else:
            prev = L[index]
            index += 1

def testRemoveRuns():
    print('Testing removeRuns...', end='')
    L = [1, 2, 3, 3]
    assert(removeRuns(L) == None)
    assert(L == [1, 2, 3])

    L = [1, 2, 3, 4]
    assert(removeRuns(L) == None)
    assert(L == [1, 2, 3, 4])

    L = [15112, 15112, 15112, 15112]
    assert(removeRuns(L) == None)
    assert(L == [15112])

    L = [ ]
    assert(removeRuns(L) == None)
    assert(L == [ ])

    print('Passed!')

testRemoveRuns()  # uncomment me to check your answer!

#####################################################
# unscrambleTreasureMap(directions, order)
#####################################################

# You have two lists containing important information. 
# The first list contains a series of directions, as such:

# [‘north’, ‘west’, ‘south’, ‘west’, ‘north’, ‘east’]

# The second list contains the order that the corresponding 
# directions should appear in, in the unscrambled list, as such:

# [3, 1, 2, 4, 5, 6]. 

# Write the function unscrambleTreasureMap(directions, order), 
# that takes in the directions and order lists and returns a list 
# containing the directions from the first list in the correct order, as such:

# ['west', 'south', 'north', 'west', 'north', 'east']

# Your function should not modify the original lists. 

def unscrambleTreasureMap(directions, order):
    ret = [None] * len(directions) 
    for index in range(len(directions)):
        ret[order[index]-1] = directions[index]
    return ret
    # return [directions[i] for i in 
    # sorted(range(0, len(directions)), key=lambda x: order[x])]

directions = ['north', 'west', 'south', 'west', 'north', 'east']
order = [3, 1, 2, 4, 5, 6]

# Check your treasure map here!
# Your function should return 'west, south, north, west, north, east'
print(unscrambleTreasureMap(directions, order))

#####################################################
# decipherScroll(scroll)
#####################################################

# Your treasure map worked perfectly and led you to an X in the sand! 
# Unfortunately, when you dig into the sand, there is not a treasure chest, 
# but a giant cave. Hopefully the treasure is in the cave somewhere! 
# Your crew adventures into the darkness and comes across a giant spider, 
# who gives you this ancient scroll:

# [3, ‘1f v’, 5, ‘ee4hne’, 6, ‘h    hne’, 2, ‘ddde’, 2, ‘0ji5’, 5, ‘     n’, 
# 0, ‘g’, 3, ‘shd ‘, 2, ‘qwm’, 1, ‘1a’, 2, ‘ksc’, 6, ‘sjdnfrh’, 0, ‘i’, 3, 
# ‘012n’, 1, ‘je’]

# The spider explains that every integer element is the index that should be 
# used to isolate a character from the string that follows it. When these 
# characters are joined together into a string, the resulting string will 
# describe where the treasure can be found. 

# Beware! There are some magical traps built into the scroll. 
# To avoid these, you must adhere to the following rules:
# You must use .join() in your solution
# You cannot build up the result in a result string, 
# since the scroll only appreciates its own writing

# Write the function decipherScroll(scroll), which takes in the scroll list 
# and returns a string with the treasure location.

def decipherScroll(scroll): return "".join([scroll[i + 1][scroll[i]] for i in range(0, len(scroll), 2)])

scroll = [3, '1f v', 5, 'ee4hne', 6, 'h    hne', 2, 'ddde', 2, '0ji5', 5, 
'     n',  0, 'g', 3, 'shd ', 2, 'qwm', 1, '1a', 2, 'ksc', 6, 'sjdnfrh', 
0, 'i', 3, '012n', 1, 'je']

# Does your solution solve the puzzle? 
# Wait until the class discusses the problem together to find out! :)
print(decipherScroll(scroll))