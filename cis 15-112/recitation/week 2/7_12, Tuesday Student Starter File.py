#################################################
# Tuesday July 12 Student Starter File
#################################################

from curses.ascii import isspace
import string

#######################################################
# collapseWhitespace
#######################################################

'''
Without using the s.replace() method, write the function collapseWhitespace(s)
that takes a string s and returns an equivalent string except that each 
occurrence of whitespace in the string is replaced by a single space. So, 
for example, collapseWhitespace("a\t\t\tb\n\nc") replaces the three tabs with a
single space, and the two newlines with another single space , returning "a b c".
'''
def collapseWhitespace(s):
    ret, prev = "", "a"
    for i in s:
        if not i.isspace():
            ret += i
        elif not prev.isspace():
            ret += " "
        prev = i 
    return ret

def testCollapseWhitespace():
    print("Testing collapseWhitespace...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    print("Passed!")

testCollapseWhitespace() # uncomment to test!
