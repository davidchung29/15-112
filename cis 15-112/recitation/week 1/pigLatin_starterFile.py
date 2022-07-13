#################################################
# Friday July 8 Recitation Student Starter
#################################################
import string

'''
This starter file contains 5 versions of the pigLatin function (named pigLatin1, 
pigLatin2, pigLatin3, etc.). Only one of these implementations is correct according to the
problem statement below. Write a test function, testPigLatin(pigLatin), which only
passes when called on the correct function. On all other functions, it should raise
an assertion error. Check your work by calling testTestPigLatin() and making sure
only one pigLatin implementation passes.

WHAT IS PIG LATIN
Pig Latin is a language game that translates English words into alternate 
versions of themselves. To translate an English word into Pig Latin, you follow 
one of two simple rules. If the word you're translating starts with one or more 
consonants, you move the consonants up to the first vowel to the back of the word, 
then follow them with 'ay'. For example, 'monkey' becomes 'onkeymay', and 'thanks'
becomes 'anksthay'. If the word starts with a vowel, you simply add 'yay' to the 
end. For example, 'apple' becomes 'appleyay'.

PIG LATIN PROBLEM STATEMENT
We wanted to write a program, pigLatin(s), which takes a string as an argument, 
translates each of the words in the string's sentence (where words are separated 
by spaces) into Pig Latin, and returns the resulting sentence. For example, 
pigLatin('how are they') should return 'owhay areyay eythay'. For now we're not 
worried about capital letters, digits, or punctuation; we only care about strings 
that contain only lowercase letters and spaces. Note: we also don't care about 
words that do not have vowels, like 'why' or 'rhythm'. It's too hard to detect 
vowel-y for now!
'''

#################################################
# Write testPigLatin here!
#################################################

def testPigLatin(pigLatin):
    # Example from problem statement
    assert(pigLatin('how are they') == 'owhay areyay eythay')
    assert(pigLatin('you trucker') == 'ouyay uckertray')
    assert(pigLatin('') == '')
    # Add more here!
    pass

###############################################################################
# Test functions
###############################################################################
# NOTE: you do not need to worry about the content of these functions.
# They test your pigLatin test cases.

def pigLatin1(s):
    if s == "":
        return ""
    result = ""
    for word in s.split():
        index = 0
        for i in range(len(word)):
            if word[i] in 'aeio':
                index = i
                break
        if index == 0:
            newWord = word + "yay"
        else:
            newWord = word[index:] + word[:index] + "ay"
        result += newWord + " "
    return result[:-1]

def pigLatin2(sent):
  res = ""
  for s in sent.split(" "):
    if(s[0] in "aeiou"):
      res += s + "yay "
    else:
      i = 0
      while(s[i] not in "aeiou"):
        i += 1
      res += s[i:] + s[0:i]
      res += "ay "
  return res[:-1]

def findFirstVowel(word):
    vowels = "aeiou"
    for i in range(len(word)):
        c = word[i]
        if c in vowels:
            break
    return i
def pigLatin3(sentence):
    vowels = "aeiou"
    result = ""
    for word in sentence.split(" "):
        if word[0] not in vowels:
            i = findFirstVowel(word)
            result += word[i:] + word[:i] + "ay" + " "
        else:
            result += word + "yay" + " "
    return result

def findVowel(word):
    vowels = "aeiou"
    for i in range(len(word)):
        if word[i] in vowels:
            return i
def pigLatin4(s):
    result = ""
    vowels = "aeiou"
    for word in s.split():
        if word.isalpha() and word == word.lower():
            if word[0] in vowels:
                toAdd = word + "yay"
            else:
                consonantIndex = findVowel(word)
                toAdd = word[consonantIndex:] + word[:consonantIndex] + "ay"
            result += toAdd + " "
    return result.strip()

def pigLatin5(s):
    result=""
    for word in s.split():
        result += (word+"yay ")
    return result.strip()

def testTestPigLatin():
    print("Testing testPigLatin()...")

    successCount = 0
    try:
        testPigLatin(pigLatin1)
        print("pigLatin1: passed")
        successCount += 1
    except:
        print("pigLatin1: failed")

    try:
        testPigLatin(pigLatin2)
        print("pigLatin2: passed")
        successCount += 1
    except:
        print("pigLatin2: failed")

    try:
        testPigLatin(pigLatin3)
        print("pigLatin3: passed")
        successCount += 1
    except:
        print("pigLatin3: failed")

    try:
        testPigLatin(pigLatin4)
        print("pigLatin4: passed")
        successCount += 1
    except:
        print("pigLatin4: failed")

    try:
        testPigLatin(pigLatin5)
        print("pigLatin5: passed")
        successCount += 1
    except:
        print("pigLatin5: failed")

    # Only one pigLatin function should pass the test cases, and it should
    # be the correct one!
    print()
    try:
        assert(successCount == 1)
        print("Success! Only 1 implementation passed your test cases.")
    except:
        print(f"FAILED: {successCount} implementations passed your "
              f"test cases.")

testTestPigLatin() # uncomment to test!

#################################################
# Fix the style
#################################################

'''
Someone with questionable stylistic taste has written nthUndulatingNumber,
which returns the nth undulating number. A number is undulating if it has at
least three digits and has the form aba[bababab...] where a does not equal b.
The program is functionally correct, but it's been written with atrocious
style. Fix this program so that it meets the 112 style guidelines without
rewriting the main logic.
'''

def is_undulating(n):
    if n < 100:
        return False
    lastDig = n % 10
    midDig = (n // 10) % 10
    firstDig = n // 100
    isAlternate = True
    while firstDig > 0:
        digit = firstDig % 10
        if isAlternate:
          if digit != lastDig:
              return False
        if (not isAlternate):
            if digit != midDig:
                return False
        isAlternate = not isAlternate
        firstDig = firstDig // 10
    return lastDig - midDig != 0

def nthUndulatingNumber(n):
    found = 0
    guess =0
    while found <= n :
        guess += 1
        if is_undulating(guess):
            found += 1
    return guess

