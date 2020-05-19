"""
Permutation in String
Solution
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].

"""

def checkInclusion(self, s1: str, s2: str) -> bool:
    
    s1Counter = Counter(s1)
    s2Counter = Counter(s2[:len(s1)-1])
    
    for i in range(len(s1)-1, len(s2)):
        
        # Storing current and start index
        current,start = i, i-len(s1)+1
        
        # Update the counter of current element in dictionary
        s2Counter[s2[current]] += 1
        
        # if count dictionary of s1 and s2 are same, then return True
        if s2Counter == s1Counter:
            return True
        
        # Update the counter of start element in dictionary
        s2Counter[s2[start]] -= 1
        
        # Remove the start element from dictionary if it's count is zero.
        if s2Counter[s2[start]] == 0:
            del s2Counter[s2[start]]
            
    return False
