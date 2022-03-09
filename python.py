"""
variables
"""
print("Range: ", end='')
numrange = int(input())
checktype = False      # True = Even, False = Odd

def evenodd(num, checkeo):
    """Check for even or odd numbers from given range"""
    if checkeo:
        if num % 2 == 0:
            print(num)
    else:
        if num%2 != 0:
            print(num)

for numbers in range(0, numrange + 1):
    evenodd(numbers, checktype)
    