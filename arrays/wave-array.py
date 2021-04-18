"""
Problem Statement:
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
Example 1:
Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5
Explanation: Array elements after 
sorting it in wave form are 
2 1 4 3 5.
 
Example 2:
Input:
N = 6
arr[] = {2,4,7,8,9,10}
Output: 4 2 8 7 10 9
Explanation: Array elements after 
sorting it in wave form are 
4 2 8 7 10 9.
Your Task:
The task is to complete the function convertToWave() which converts the given array to wave array.
"""
def convertToWave(array):
    N = len(array)
    i=0
    while(i<N):
        # if i is already at last value no need to swap
        if (i+1)<N:
            #swap by addition
            array[i] = array[i]+array[i+1]
            array[i+1] = array[i]-array[i+1]
            array[i] = array[i]-array[i+1]
        i+=2
    print(array)
convertToWave([1,2,3,4,5,6])

# Since the array is sorted we just need to swap every other value with the next element