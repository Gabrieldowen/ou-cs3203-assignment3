

def summation(numList):
    total = 0
    for num in numList:
        total += num

    return total

numList = [1, 2, 3, 4, 5, 6, 7]

sum = summation(numList)
print("the sum is " + str(sum))
