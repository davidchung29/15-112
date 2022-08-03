#################################################
# hw10.py:
#
# Your name:
# Your andrew id:
#################################################

import cs112_n22_week4_linter

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

def getPairSum(L, target):
    for number in L:
        L.remove(number)
        # check if counterpart is in L
        if target-number in L:
            return number, target-number

def containsPythagoreanTriple(L):
    # create a list where each element is squared
    sqL = [x**2 for x in L]
    for target in sqL:
        sqL2= sqL[:]
        sqL2.remove(target)
        for number in sqL2:
            if target-number in sqL2:
                return True
    return False

def movieAwards(oscarResults):
    result = dict()
    for movie in oscarResults:
        if movie[1] not in result.keys():
            result[movie[1]] = 1
        else:
            result[movie[1]] += 1
    return result

def friendsOfFriends(friends):
    # iterate through each person
    result = {}
    for person in friends:
        result[person] = set()
        #iterate through each friend
        for friend in friends[person]:
            # iterate through each friends' friend
            for friendsFriend in friends[friend]:
                if friendsFriend not in friends[person]:
                    if friendsFriend != person:
                        result[person].add(friendsFriend)
    return result



#################################################
# Test Functions
#################################################


def testGetPairSum():
    print("Testing getPairSum()...", end="")
    assert(getPairSum([1], 1) == None)
    assert(getPairSum([5, 2], 7) in [ (5, 2), (2, 5) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 2) in
                      [ (10, -8), (-8, 10),(-1, 3), (3, -1), (1, 1) ])
    assert(getPairSum([10, -1, 1, -8, 3, 1], 10) == None)
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, 0, 5], 10) in
                      [ (10, 0), (0, 10)] )
    assert(getPairSum([10, -1, 1, -8, 3, 1, 8, 19, -9, 5], 10) in
                      [ (19, -9), (-9, 19)] )
    assert(getPairSum([1, 4, 3], 2) == None) # catches reusing values! 1+1...
    print("Passed!")

def testContainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...", end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4]) == True)
    assert(containsPythagoreanTriple([1,2,3,4,5,6,7,8,9,10,11]) == True)
    assert(containsPythagoreanTriple([1,3,6,2,8,1,4]) == False)
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,728,4])
                                      == True) # 54, 728, 730
    assert(containsPythagoreanTriple([1,730,3,6,54,2,8,1,729,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                6253, 7800, 9997]) == True) # 6253, 7800, 9997
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9998]) == False)
    assert(containsPythagoreanTriple([1,731,3,6,54,2,8,1,728,4,
                                      6253, 7800, 9996]) == False)
    print("Passed!")

def testMovieAwards():
    print('Testing movieAwards()...', end='')
    tests = [
      (({ ("Best Picture", "The Shape of Water"), 
          ("Best Actor", "Darkest Hour"),
          ("Best Actress", "Three Billboards Outside Ebbing, Missouri"),
          ("Best Director", "The Shape of Water") },),
        { "Darkest Hour" : 1,
          "Three Billboards Outside Ebbing, Missouri" : 1,
          "The Shape of Water" : 2 }),
      (({ ("Best Picture", "Moonlight"),
          ("Best Director", "La La Land"),
          ("Best Actor", "Manchester by the Sea"),
          ("Best Actress", "La La Land") },),
        { "Moonlight" : 1,
          "La La Land" : 2,
          "Manchester by the Sea" : 1 }),
      (({ ("Best Picture", "12 Years a Slave"),
          ("Best Director", "Gravity"),
          ("Best Actor", "Dallas Buyers Club"),
          ("Best Actress", "Blue Jasmine") },),
        { "12 Years a Slave" : 1,
          "Gravity" : 1,
          "Dallas Buyers Club" : 1,
          "Blue Jasmine" : 1 }),
      (({ ("Best Picture", "The King's Speech"),
          ("Best Director", "The King's Speech"),
          ("Best Actor", "The King's Speech") },),
        { "The King's Speech" : 3}),
      (({ ("Best Picture", "Spotlight"), ("Best Director", "The Revenant"),
          ("Best Actor", "The Revenant"), ("Best Actress", "Room"),
          ("Best Supporting Actor", "Bridge of Spies"),
          ("Best Supporting Actress", "The Danish Girl"),
          ("Best Original Screenplay", "Spotlight"),
          ("Best Adapted Screenplay", "The Big Short"),
          ("Best Production Design", "Mad Max: Fury Road"),
          ("Best Cinematography", "The Revenant") },),
        { "Spotlight" : 2,
          "The Revenant" : 3,
          "Room" : 1,
          "Bridge of Spies" : 1,
          "The Danish Girl" : 1,
          "The Big Short" : 1,
          "Mad Max: Fury Road" : 1 }),
       ((set(),), { }),
            ]
    for args,result in tests:
        if (movieAwards(*args) != result):
            print('movieAwards failed:')
            print(args)
            print(result)
            assert(False)
    print('Passed!')

def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = dict()
    d["fred"] = set(["wilma", "betty", "barney", "bam-bam"])
    d["wilma"] = set(["fred", "betty", "dino"])
    d["betty"] = d["barney"] = d["bam-bam"] = d["dino"] = set()
    fof = friendsOfFriends(d)
    assert(fof["fred"] == set(["dino"]))
    assert(fof["wilma"] == set(["barney", "bam-bam"]))
    result = { "fred":set(["dino"]),
               "wilma":set(["barney", "bam-bam"]),
               "betty":set(),
               "barney":set(),
               "dino":set(),
               "bam-bam":set()
             }
    assert(fof == result)
    d = dict()
    #                A    B    C    D     E     F
    d["A"]  = set([      "B",      "D",        "F" ])
    d["B"]  = set([ "A",      "C", "D",  "E",      ])
    d["C"]  = set([                                ])
    d["D"]  = set([      "B",            "E",  "F" ])
    d["E"]  = set([           "C", "D"             ])
    d["F"]  = set([                "D"             ])
    fof = friendsOfFriends(d)
    assert(fof["A"] == set(["C", "E"]))
    assert(fof["B"] == set(["F"]))
    assert(fof["C"] == set([]))
    assert(fof["D"] == set(["A", "C"]))
    assert(fof["E"] == set(["B", "F"]))
    assert(fof["F"] == set(["B", "E"]))
    result = { "A":set(["C", "E"]),
               "B":set(["F"]),
               "C":set([]),
               "D":set(["A", "C"]),
               "E":set(["B", "F"]),
               "F":set(["B", "E"])
              }
    assert(fof == result)
    print("Passed!")

def testAll():
    testGetPairSum()
    testContainsPythagoreanTriple()
    testMovieAwards()
    testFriendsOfFriends()

#################################################
# main
#################################################

def main():
    cs112_n22_week4_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
