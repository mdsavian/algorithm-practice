"""
LeetCode 392. Is Subsequence

https://leetcode.com/problems/is-subsequence/

"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)


def test(s, t, expected_answer):
    answer = Solution().isSubsequence(s, t)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test("ab", "baab", True)
test("ace", "abcde", True)
test("aec", "abcde", False)
test("abc", "ahbgdc", True)
test("axc", "ahbgdc", False)
