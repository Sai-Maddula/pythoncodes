"""
source:leetcode
Given a string s, find the length of the longest substring without repeating characters.
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def longestNonRepeatingSubString(s:str)-> int:
    char_dict={}
    start=0
    max_length=0
    for ind,character in enumerate(s):
        if character in char_dict and start <= char_dict[character]:
            start = char_dict[character]+1
            
        else:
            max_length=max(max_length,ind-start+1)
        char_dict[character]=ind
            
    return max_length

#--- Driver Codee ---#
s= input("Enter string: ").strip()
print(longestNonRepeatingSubString(s))