"""
Math 560
Project 1
Fall 2021

Partner 1: Zedong Gao (zg79)
Partner 2: Yunbo Liu (yl815)
Date:10/27/2021
"""

"""
SelectionSort
"""
def SelectionSort(listToSort):
    for i in range(len(listToSort)):
        temp = listToSort[i]
        index = i
        for j in range(i, len(listToSort)):
            if temp > listToSort[j]:
                temp = listToSort[j]
                index = j
        listToSort[index] = listToSort[i]
        listToSort[i] = temp
    return listToSort

"""
InsertionSort
"""
def InsertionSort(listToSort):
    for i in range(1, len(listToSort)):
        key = listToSort[i]
        j = i - 1
        while j >= 0 and listToSort[j] > key:
            listToSort[j + 1] = listToSort[j]
            j = j - 1
        listToSort[j + 1] = key
    return listToSort

"""
BubbleSort
"""
def BubbleSort(listToSort):
    for i in range(len(listToSort)):
        status = 1
        for j in range(0, len(listToSort) - i - 1):
            if listToSort[j] > listToSort[j + 1]:
                temp = listToSort[j]
                listToSort[j] = listToSort[j + 1]
                listToSort[j + 1] = temp
                status = 0
        if status == 1:
            break
    return listToSort

"""
MergeSort
"""
def MergeSort(listToSort):
    if len(listToSort) == 1:
        return listToSort
    elif len(listToSort) == 2:
        if listToSort[0] > listToSort[1]:
            temp = listToSort[0]
            listToSort[0] = listToSort[1]
            listToSort[1] = temp
        return listToSort
    else:
        mid = len(listToSort) // 2
        left = listToSort[:mid]
        right = listToSort[mid:]
        MergeSort(left)
        MergeSort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                listToSort[k] = left[i]
                i = i + 1
            else:
                listToSort[k] = right[j]
                j = j + 1
            k = k + 1
        if i == len(left):
            while j < len(right):
                listToSort[k] = right[j]
                j = j + 1
                k = k + 1
        else:
            while i < len(left):
                listToSort[k] = left[i]
                i = i + 1
                k = k + 1
        return listToSort

"""
QuickSort

Sort a list with the call QuickSort(listToSort),
or additionally specify i and j.
"""
def QuickSort(listToSort, i=0, j=None):
    # Set default value for j if None.
    if j == None:
        j = len(listToSort)
    if j - i == 1:
        return listToSort
    pivot = i
    cursor = i + 1
    left = i + 1
    right = j
    while left < right:
        if listToSort[left] < listToSort[pivot]:
            temp = listToSort[left]
            listToSort[left] = listToSort[cursor]
            listToSort[cursor] = temp
            cursor = cursor + 1
        left = left + 1
    temp = listToSort[pivot]
    listToSort[pivot] = listToSort[cursor - 1]
    listToSort[cursor - 1] = temp
    pivot = cursor - 1
    if i < pivot + 1:
        QuickSort(listToSort, i, pivot + 1)
    if pivot + 1 < j:
        QuickSort(listToSort, pivot + 1, j)
    return listToSort

"""
Importing the testing code after function defs to ensure same references.
"""
from project1tests import *

"""
Main function.
"""
if __name__ == "__main__":
    print('Testing Selection Sort')
    print()
    testingSuite(SelectionSort)
    print()
    print('Testing Insertion Sort')
    print()
    testingSuite(InsertionSort)
    print()
    print('Testing Bubble Sort')
    print()
    testingSuite(BubbleSort)
    print()
    print('Testing Merge Sort')
    print()
    testingSuite(MergeSort)
    print()
    print('Testing Quick Sort')
    print()
    testingSuite(QuickSort)
    print()
    print('UNSORTED measureTime')
    print()
    measureTime()
    print()
    print('SORTED measureTime')
    print()
    measureTime(True)