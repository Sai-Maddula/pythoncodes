"""
Given an Array find the max and second max element in the array
"""

def largestAndSecondLargest(arr):
    if len(arr) < 2 :
        return [arr[0],-1]
    maxelem = max(arr)
    secondmax= -maxelem
    for i in arr:
        if i > secondmax and i != maxelem:
            secondmax = i
    return [maxelem,secondmax]

print(largestAndSecondLargest([56,7,92,123,72,98]))