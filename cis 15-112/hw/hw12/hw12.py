#################################################
# hw12.py
#
# Your name:
# Your andrew id:
#################################################

from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF
import cs112_n22_hw12_linter
import math, copy

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

def evalPrefixNotation(L):
    if len(L) == 1:
        return L[0]
    for element in L:
        if not isinstance(element, int):
            if element not in ["+", "-", "*"]:
                raise Exception('Unknown operator: ' + operator)
    L1 = []
    operator = L.pop(0)
    intCount = 0
    opCount = 1
    while intCount != opCount:
        value = L.pop(0)
        if isinstance(value, int):
            intCount += 1
        else:
            opCount += 1
        L1.append(value)
    if operator == "+":
        return evalPrefixNotation(L1) + evalPrefixNotation(L)
    elif operator == "-":
        return evalPrefixNotation(L1) - evalPrefixNotation(L)
    elif operator == "*":
        return evalPrefixNotation(L1) * evalPrefixNotation(L)


'''def possibleMoves(rows, cols, crow, ccol):
    xmove = (2, -2, 1, -1)
    ymove = ((1, -1), (1, -1), (2, -2), (2, -2))
    possibleCoords = []
    for x in range(len(xmove)):
        for y in range(len(ymove[x])):
            if ((crow + xmove[x] < rows) and (ccol + ymove[x][y] < cols)):
                possibleCoords.append((xmove[x], ymove[y]))
    return possibleCoords'''

def printBoard(board):
    for row in board:
        print(row)

def knightsTourHelper(rows, cols, crow, ccol, visited, count):
    possMoves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]
    for row in visited:
        for element in row:
            if element == (rows*cols):
                return visited
    for move in possMoves:
        drow = move[0]
        dcol = move[1];
        tempRow = crow + drow
        tempCol = ccol + dcol
        if ((0 <= tempRow < rows) and (0 <= tempCol < cols)):
            if (visited[tempRow][tempCol] == 0):
                #print("hi")
                count += 1
                visited[tempRow][tempCol] = count
                if knightsTourHelper(rows, cols, tempRow, tempCol, 
                                                 visited, count):
                    #print("1")
                    return visited
                count -= 1 
                visited[tempRow][tempCol] = 0
    return None

def knightsTour(rows, cols):
    board = [[0] * cols for _ in range(rows)]
    board[0][0] = 1
    result = knightsTourHelper(rows, cols, 0, 0, board, 1)
    return result

#################################################
# Test Functions
#################################################

def testEvalPrefixNotation():
    print('Testing evalPrefixNotation()...', end='')
    assert(evalPrefixNotation([42]) == 42)          # (42)
    assert(evalPrefixNotation(['+', 3, 4]) == 7)    # (3 + 4)
    assert(evalPrefixNotation(['-', 3, 4]) == -1)   # (3 - 4)
    assert(evalPrefixNotation(['-', 4, 3]) == 1)    # (4 - 3)
    assert(evalPrefixNotation(['+', 3, '*', 4, 5]) == 23)   # (3 + (4 * 5))

    # ((2 * 3) + (4 * 5))
    assert(evalPrefixNotation(['+', '*', 2, 3, '*', 4, 5]) == 26)
    # ((2 + 3) * (4 + 5))
    assert(evalPrefixNotation(['*', '+', 2, 3, '+', 4, 5]) == 45)
    # ((2 + (3 * (8 - 7))) * ((2 * 2) + 5))
    assert(evalPrefixNotation(['*', '+', 2, '*', 3, '-', 8, 7,
                               '+', '*', 2, 2, 5]) == 45)
    
    #Make sure to raise an error for operators that are not +, -, or *
    raisedAnError = False
    try:
        evalPrefixNotation(['^', 2, 3])
    except:
        raisedAnError = True
    assert(raisedAnError == True)
    print('Passed.')


def testKnightsTour():
    print('Testing knightsTour()....', end='')
    def checkDims(rows, cols, ok=True):
        T = knightsTour(rows, cols)
        s = f'knightsTour({rows},{cols})'
        if (not ok):
            if (T is not None):
                raise Exception(f'{s} should return None')
            return True
        if (T is None):
            raise Exception(f'{s} must return a {rows}x{cols}' +
                             ' 2d list (not None)')
        if ((rows != len(T)) or (cols != (len(T[0])))):
            raise Exception(f'{s} must return a {rows}x{cols} 2d list')
        d = dict()
        for r in range(rows):
            for c in range(cols):
                d[ T[r][c] ] = (r,c)
        if (sorted(d.keys()) != list(range(1, rows*cols+1))):
            raise Exception(f'{s} should contain numbers' +
                             ' from 1 to {rows*cols}')
        prevRow, prevCol = d[1]
        for step in range(2, rows*cols+1):
            row,col = d[step]
            distance = abs(prevRow - row) + abs(prevCol - col)
            if (distance != 3):
                raise Exception(f'{s}: from {step-1} to {step}' +
                                 ' is not a legal move')
            prevRow, prevCol = row,col
        return True
    assert(checkDims(4, 3))
    assert(checkDims(4, 4, ok=False))
    assert(checkDims(4, 5))
    assert(checkDims(3, 4))
    assert(checkDims(3, 6, ok=False))
    assert(checkDims(3, 7))
    assert(checkDims(5, 5))
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testEvalPrefixNotation()
    testKnightsTour()
def main():
    cs112_n22_hw12_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
