"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
Example 1:
Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:
Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and returns the sum of subarray with maximum sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def maxContiguousSubArraySum(arr):
    maxima = -10**7
    local_maxima = 0
    for elem in arr:
        local_maxima += elem
        if local_maxima>maxima:
            maxima=local_maxima
        #making 0 so that we will not consider consecutive negative numbers 
        if local_maxima<0:
            local_maxima=0
    print(maxima)
maxContiguousSubArraySum([-1,-2,-3,-4])