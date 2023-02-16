
# finds and returns the sum of the array
def summation(numList):
    total = 0
    for num in numList:
        total += num

    return total

# finds and returns product of array
def product(numList):
    total = 1
    for num in numList:
        total *= num

    return total

# main
numList = []

sizeList = int(input("\nenter the size of the list: "))
print("\ninput " + str(sizeList) + " numbers", )

for i in range(sizeList):
    numList.append(int(input()))

# function calls
finalSum = summation(numList)
finalProduct = product(numList)

# final output
print("\nthe sum is " + str(finalSum))
print("\nthe product is " + str(finalProduct))
