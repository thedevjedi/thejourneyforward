#!/usr/bin/env python3

def linear_search(list, key):
    for i, item in enumerate(list):
        if item == key:
            return i
    return "Not found."

def binary_search(list, key):
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return "Found"
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return "Not Found."

def sort_list(list):
    return list.sort()

def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)

print(binary_search(cars, "Ford"))
print(binary_search(cars, "Fords"))



