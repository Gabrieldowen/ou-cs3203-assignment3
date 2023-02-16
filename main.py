

def summation(numList):
    total = 0
    for num in numList:
        total += num

    return total

def product(numList):
    total = 1
    for num in numList:
        total *= num

    return total

numList = [1, 2, 3, 4, 5, 6, 7]

finalSum = summation(numList)
finalProduct = product(numList)
print("the sum is " + str(finalSum))
print("the product is " + str(finalProduct))
