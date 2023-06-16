"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

THE IDEIA OF CREATING HASHMAPS IS CORRECT, BUT HAVE A BETTER SOLUTION, 

WHEN REPEAT TRY TO THINK HOW YOU CAN REDUCE THE NUMBER OF FORS

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        tMap, sMap = {}, {}

        for i in s:
            if i in sMap:
                sMap[i] += 1
            else:
                sMap[i] = 1

        for i in t:
            if i in tMap:
                tMap[i] += 1
            else:
                tMap[i] = 1

        for key in tMap:
            if not key in sMap or tMap[key] != sMap[key]:
                return False

        return True
