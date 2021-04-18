"""
Minimum distance between two numbers
You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.
Input :
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. The first line of each test case contains an integer N denoting size array. Then in the next line are N space separated values of the array A. The last line of each test case contains two integers  x and y.
Output :
Print the minimum index based distance between x and y.
Your Task:
Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array. If no such distance is possible then return -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= A[i], x, y <= 105


Example:
Sample Input:
2
4
1 2 3 2
1 2
7
86 39 90 67 84 66 62
42 12
Sample Output:
1
-1
Explanation:
Testcase1: x = 1 and y = 2. There are two distances between x and y, which are 1 and 3 out of which the least is 1.
Testcase2: x = 42 and y = 12. We return -1 as x and y don't exist in the array.
"""

# def minimumDistanceBetweenGivenNumbers(arr,num1,num2):
#     num1_indices=[]
#     num2_indices=[]
#     if num1 not in arr or num2 not in arr :
#         print("-1")
#     else:
#         for pos,elem in enumerate(arr):
#             if elem == num1:
#                 num1_indices.append(pos)
#             elif elem == num2:
#                 num2_indices.append(pos)
#         minimum=len(arr)+1
#         for i in num1_indices:
#             for j in num2_indices:
#                 if abs(i-j)<minimum:
#                     minimum = abs(i-j)
#         print(minimum)
# minimumDistanceBetweenGivenNumbers([1,3,3,2,2,6,5,4,1,3,2,6,1],1,2)
import sys

def minDist(arr,n,x,y):
    i=0
    p=-1
    minDistance = len(arr)+1

    for i in range(n):
        print(i,p,minDistance)
        if arr[i] == x or arr[i] == y:
            if p!=-1 and arr[i]!=arr[p]:
                minDistance = min(minDistance,i-p)
        p=i
    if p == len(arr)+1:
        return -1
    return minDistance
arr = [3, 5, 4, 2, 6, 3, 0, 0, 5, 4, 8, 3]
n = len(arr)
x = 3
y = 6
print ("Minimum distance between %d and %d is %d\n"%( x, y,minDist(arr, n, x, y)))

# This code is contributed by Shreyanshi Arun.
