#################################################
# hw3.py
# name: David Chung
# andrew id: dichung
# section A
#################################################

import cs112_n22_week2_linter
import math, string, random

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

# create a string that contains all the substrings of n
def allSubstrings(n): 
  subStrings = ""
  for firstIndex in range(len(n)+1):
    for lastIndex in range(firstIndex, len(n)+1):
      subStrings += n[firstIndex:lastIndex:] + " "
      subStrings.strip()
  return subStrings

#check if a string is a palindrome
def isPalindrome(s):
  if s[::-1] == s:
    return True
  return False

#remove all whitespace in a string 
def removeWhiteSpace(s):
  result = ""
  for character in s:
    if not character.isspace():
      result += character
  return result

# find the number of exact matches between two strings
def exactMatches(s1, s2):
    count = 0
    index = 0
    while len(s1) > 0 and index < len(s2):
        if s1[index] == s2[index]:
            count += 1
            s1 = s1[:index:] + s1[index+1::]
            s2 = s2[:index:] + s2[index+1::]
        #reset index because strings were sliced
            index = 0  
        else:
            index += 1
    return count

# find the number of partial matches between  two strings
def partialMatches(s1, s2):
    count = 0
    for element in s1: #for the numbers remaining in guess
        if element in s2:
            count += 1
            s1.replace(element, '')
            s2.replace(element, '')
    return count

#################################################
# hw3-standard-functions
#################################################

# find largest number in string
def largestNumber(s):
    high = 0
    number = 0
    s += " "
    for element in s:
        if element.isdigit():
            number *= 10
            number += int(element)
        if (not element.isdigit() or element == " "):
            if number > high:
              high = number
            number = 0
    if high > 0:
      return high
    
# rotate elements in string to left
def rotateStringLeft(s, n):
    if n==0 or s == '':
        return s
    n = n % len(s)
    firstHalf = s[n::]
    secondHalf = s[0:n:]
    return firstHalf + secondHalf

# check if one string is a roation of another
def isRotation(s,t):
    n = 1
    if len(s) == len(t) and s != t:
        while s != t and n<len(s):
            s = rotateStringLeft(s, n)
            n+=1
        if s == t:
            return True
    return False
# find longest palindrome in a substring
def longestSubpalindrome(s):
    subStrings = allSubstrings(s).split()
    subPalindrome = ""
    for subString in subStrings:
        if isPalindrome(subString):
            if len(subString) > len(subPalindrome):
                subPalindrome = subString
            elif (len(subString) == len(subPalindrome)): # if length is same
                # make sure newly found substring is greater
                if (subString > subPalindrome):
                    subPalindrome = subString
    return subPalindrome

# replace characters in pattern with a message
def patternedMessage(msg, pattern):
    result = ""
    msg = removeWhiteSpace(msg)
    currentPlace = 0#which letter in msg you are on
    for character in pattern:
        if character.isspace():
            result += character
        else:
            result += msg[currentPlace]
            currentPlace = (currentPlace + 1)%(len(msg))
    return result.strip()

#calculate how close two strings are (mastermind)
def mastermindScore(target, guess):
    lengthInit = len(guess) #initial length of guess
  
    exactCount = exactMatches(target, guess)
    partialCount = partialMatches(target, guess) - exactCount
    if exactCount > 0 or partialCount > 0:
        result = ""

        if exactCount == lengthInit:
            return "You win!!!"
        if exactCount == 1:
            if partialCount > 0:
                result += "1 exact match, "
            else: #partial is empty = no comma
                result += "1 exact match"
        elif exactCount > 0:
            if partialCount > 0:
                result += f"{exactCount} exact matches, "
            else: #partial is empty = no comma
                result += f"{exactCount} exact matches"
        if partialCount == 1:
            result += "1 partial match"
        elif partialCount > 0:
            result += f"{partialCount} partial matches"
        return result
    return "No matches"



#################################################
# hw3-bonus-functions
# these are optional
#################################################

def encodeRightLeftRouteCipher(text, rows):

    
    return 42

def decodeRightLeftRouteCipher(cipher):
    return 42




def topLevelFunctionNames(code):
    return 42




def getEvalSteps(expr):
    return 42


#################################################
# Test Functions
#################################################

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    assert(largestNumber("42!!!!") == 42)
    assert(largestNumber("12+3==15") == 15)
    assert(largestNumber("12dogs345cats67owls") == 345)
    assert(largestNumber("") == None)
    assert(largestNumber("There are more than 20 studennts in 15-112") == 112)
    assert(largestNumber("This is homework 3 and not 2") == 3)
    print("Passed!")

def testRotateStringLeft():
    print('Testing rotateStringLeft()...', end='')
    assert(rotateStringLeft('abcde', 0) == 'abcde')
    assert(rotateStringLeft('abcde', 1) == 'bcdea')
    assert(rotateStringLeft('abcde', 2) == 'cdeab')
    assert(rotateStringLeft('abcde', 3) == 'deabc')
    assert(rotateStringLeft('abcde', 4) == 'eabcd')
    assert(rotateStringLeft('abcde', 5) == 'abcde')
    assert(rotateStringLeft('abcde', 25) == 'abcde')
    assert(rotateStringLeft('abcde', 28) == 'deabc')
    assert(rotateStringLeft('abcde', -1) == 'eabcd')
    assert(rotateStringLeft('abcde', -24) == 'bcdea')
    assert(rotateStringLeft('abcde', -25) == 'abcde')
    assert(rotateStringLeft('abcde', -26) == 'eabcd')
    assert(rotateStringLeft('ABCDEF', -2) == 'EFABCD')
    assert(rotateStringLeft('ABCDEFGHIJKLMNOP', -4) == 'MNOPABCDEFGHIJKL')
    assert(rotateStringLeft('ASDFGH', 3) == 'FGHASD')
    assert(rotateStringLeft('', -26) == '')
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()...', end='')
    assert(isRotation('a', 'a') == False) # a string is not a rotation of itself
    assert(isRotation('', '') == False) # a string is not a rotation of itself
    assert(isRotation('ab', 'ba') == True)
    assert(isRotation('abcd', 'dabc') == True)
    assert(isRotation('abcd', 'cdab') == True)
    assert(isRotation('abcd', 'bcda') == True)
    assert(isRotation('abcd', 'abcd') == False)
    assert(isRotation('abcd', 'dcba') == False)
    assert(isRotation('abcd', 'bcd') == False)
    assert(isRotation('abcd', 'bcdx') == False)
    assert(isRotation('abcdefg', 'bcdefga') == True)
    assert(isRotation('123456', '412356') == False)
    print('Passed!')

def testLongestSubpalindrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") == "cbc")
    assert(longestSubpalindrome("aba") == "aba")
    assert(longestSubpalindrome("a") == "a")
    assert(longestSubpalindrome("") == "")
    assert(longestSubpalindrome("abcdcbefe") == "bcdcb")
    assert(longestSubpalindrome("edcabbbacde") == "edcabbbacde")
    assert(longestSubpalindrome("abaasdfhghfd") == "dfhghfd")
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")
    assert(patternedMessage("abc def",   "***** ***** ****")   ==
           "abcde fabcd efab")
    assert(patternedMessage("hello this is a test",   
    "** ** ** ** ** ** ** **")   ==
           "he ll ot hi si sa te st")
    assert(patternedMessage("abc def", "\n***** ***** ****\n") == 
           "abcde fabcd efab")

    parms = [
    ("Go Pirates!!!", """
***************
******   ******
***************
"""),
    ("Three Diamonds!","""
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""),
    ("Go Steelers!","""
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
    solns = [
"""
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
,
"""
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
,
"""
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    ]
    parms = [("A-C D?", """
*** *** ***
** ** ** **
"""),
    ("A", "x y z"),
    ("The pattern is empty!", "")
    ]
    solns = [
"""
A-C D?A -CD
?A -C D? A-
""",
"A A A",
""
    ]
    for i in range(len(parms)):
        (msg,pattern) = parms[i]
        soln = solns[i]
        soln = soln.strip("\n")
        observed = patternedMessage(msg, pattern)
        assert(observed == soln)
    print("Passed!")

def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')
    assert(mastermindScore('helloooo', 'helloooo') ==
                           'You win!!!')
    assert(mastermindScore('15-112', '15-110') ==
                           '5 exact matches')
    print("Passed!")


def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")



def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # hw3-standard
    testLargestNumber()
    testRotateStringLeft()
    testIsRotation()
    testLongestSubpalindrome()
    testPatternedMessage()
    testMastermindScore()


    # hw3-bonus
    # testEncodeAndDecodeRightLeftRouteCipher()
    # testTopLevelFunctionNames()
    # testGetEvalSteps()

def main():
    cs112_n22_week2_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
