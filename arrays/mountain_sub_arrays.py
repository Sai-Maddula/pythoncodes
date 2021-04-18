"""
Mountain Subarray Problem 
We are given an array of integers and a range, we need to find whether the subarray which falls in this range has values in the form of a mountain or not. 
All values of the subarray are said to be in the form of a mountain if either all values are increasing or decreasing or first increasing and then decreasing.
 More formally a subarray [a1, a2, a3 … aN] is said to be in form of a mountain if there exists an integer K, 1 <= K <= N such that,
a1 <= a2 <= a3 .. <= aK >= a(K+1) >= a(K+2) …. >= aN
You have to process Q queries. In each query you are given two integer L and R, denoting starting and last index of the subarrays respectively.
Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the array. The following line contains N space-separated integers forming the array. Next line contains an integer Q, denoting the number of queries. For each query, you are given two space-separated integers L and R in a new line. 
Output:
For each query, print "Yes" (without quotes) if the subarray is in mountain form, otherwise print "No" (without quotes) in a new line.
"""

def mountain_sub_array(arr,Left_index,Right_index):
    sub_array = arr[Left_index:Right_index+1]
    result = "No"

    sorted_sub_array= sorted(sub_array)
    if sorted_sub_array == sub_array or sorted_sub_array[::-1]==sub_array:
        result ="Yes"
    else:
        max_value_index = sub_array.index(sorted_sub_array[-1])
        left = sub_array[:max_value_index]
        right = sub_array[max_value_index:]
        if sorted(left) == left and sorted(right,reverse=True) ==right:
            result = "Yes"
    print(f"sub_array:{sub_array}, is-mountain: {result}")

mountain_sub_array([2,3,2,4,4,6,3,2],1,3)







# If all values are in increasing order i.e the subarray must be in ascending order
    # We can check verify this by sorting the array and check if its the same
    #same applies for decreasing order

#if there is increasing and then decreasing order there must be max value existing between and boundaries,
    #  also the left side of max has to be increasing and Right side of max has to be decreasing