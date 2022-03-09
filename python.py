from tabnanny import check


numRange = int(input())
checkType = True      # True = Even, False = Odd

def evenOdd(num, checkType):
    if checkType == True:
        if num % 2 == 0:
            print(num)
    else:
        if num%2 != 0:
            print(num)

for numbers in range(0, numRange + 1):
        evenOdd(numbers, checkType)
    