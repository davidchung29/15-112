def isPrime(n):
    if n<2:
        return False
    for factor in range(2,n):
        if n%factor == 0:
            return False
    return True

def areSexyPrimes(n,m):
    if type(n) == int and type(m) == int:
        if n>0 and m>0:
            if isPrime(n) and isPrime(m):
                if abs(n-m) == 6:
                    return True
    return False

def testAreSexyPrimes():
    print("Testing areSexyPrimes...", end="")
    assert(areSexyPrimes(3, 9) == False)
    assert(areSexyPrimes(5, 11) == True)
    assert(areSexyPrimes(7, 13) == True)
    assert(areSexyPrimes(461, 467) == True)
    assert(areSexyPrimes(123, 112) == False)
    assert(areSexyPrimes(5.0, 11) == False)
    assert(areSexyPrimes(-2, 8) == False)
    assert(areSexyPrimes('yup', 'boi') == False)
    print("Passed!")






testAreSexyPrimes()