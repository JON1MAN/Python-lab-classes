#!/Users/amarchuk/Documents/GitHub/Andrew/.venv/python_lab_classes/bin/python

import random
from enum import Enum

class SortingOrder(Enum):
    ASC = "ascending",
    DESC = "descending"

def quickSort(nums, sortingOrder):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = []
    middle = []
    right = []

    for x in nums:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            middle.append(x)

    if sortingOrder == SortingOrder.ASC:
        return quickSort(left, SortingOrder.ASC) + middle + quickSort(right, SortingOrder.ASC)
    elif sortingOrder == SortingOrder.DESC:
        return quickSort(right, SortingOrder.DESC) + middle + quickSort(left, SortingOrder.DESC)
    else:
        raise ValueError("order must be 'ASC' or 'DESC'")

def sortedCorrectly(originalArray, sortedArray, sortingOrder):
    if sortingOrder == SortingOrder.ASC:
        return sortedArray == sorted(originalArray)
    elif sortingOrder == SortingOrder.DESC:
        return sortedArray == sorted(originalArray, reverse=True)
    else:
        return False, " Unknown order"

nums = [random.randint(1, 100) for _ in range(50)]
print(nums)
sortingOrder = SortingOrder.DESC
sortedNums = quickSort(nums, sortingOrder)
print(sortedNums)

if sortedCorrectly(nums, sortedNums, sortingOrder):
    print("QuickSort result matches Python library sort")
else:
    print("QuickSort result does NOT match library sort")