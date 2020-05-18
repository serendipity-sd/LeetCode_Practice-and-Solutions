"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp, S, P , A = len(s), len(p), 0, 0, []
        
        if lp> ls: 
            return []  ## as the anagram wont exist 
        
        for i in range(lp):
            S = S+ hash(s[i])
            P = P+ hash(p[i])
        if S == P: 
            A.append(0)
                
        for i in range(lp, ls): 
            S = S + hash(s[i]) - hash(s[i-lp])
            
            if S == P: 
                A.append(i-lp+1)  # for the beginning string position
                
        return A