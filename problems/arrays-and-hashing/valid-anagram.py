"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sHash = {}
        tHash = {}

        for i in range(len(s)):
            sHash[s[i]] = 1 + sHash.get(s[i], 0)
            tHash[t[i]] = 1 + tHash.get(t[i], 0)

        return sHash == tHash


def test(s, t, expected_answer):
    answer = Solution().isAnagram(s, t)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test("xx", "xxx", False)
test("anagram", "nagaram", True)
test("ant", "tan", True)
test("rat", "car", False)
