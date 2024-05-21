def binary_search(list, target):
    """ create 2 variables to point to the biginning and end of the list """
    first = 0
    last = len(list) - 1

    """ Here we implement a while loop so that it keeps executing until the value of first is equal o less than the value of last """
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)
