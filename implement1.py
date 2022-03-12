"""
Implementing y = |x|
"""


def eq(sec):
    """
        Function to return the value of y for every X given
    """
    return abs(sec)

for x in range(-5, 5):      # Given range of inputs for X cord
    print(" X:{} and Y:{}".format(x, eq(x)) )       # Print X and Y values

