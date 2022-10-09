def swapList(newList) :
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp

    return newList

newList = []
newList = [int(item) for item in input("Enter the list items : ").split()]

print(swapList(newList))