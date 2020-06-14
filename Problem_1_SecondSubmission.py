###Finding the Square Root of an Integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    if number == 0:
        return 0

    low = 0
    high = number

    num = sqrt_rec(low, high, number)
    return num

def sqrt_rec(low, high, number):
    if low == high:
        return low

    guess = (low + high) // 2

    if guess ** 2 > number:
        return sqrt_rec(low, guess - 1, number)
    elif guess ** 2 < number:
        return sqrt_rec(guess + 1, high, number)
    else:
        print(guess)
        return guess

#Edge cases
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if (244 == sqrt(60000)) else "Fail")
#Cases
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
