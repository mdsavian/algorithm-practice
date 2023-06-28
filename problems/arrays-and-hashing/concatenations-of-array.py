"""
LeetCode 1929. Concatenation of Array

https://leetcode.com/problems/concatenation-of-array/

"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums)*2)]

        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + len(nums)] = n

        return ans


def test(s, expected_answer):
    answer = Solution().getConcatenation(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test([1, 2, 1], [1, 2, 1, 1, 2, 1])
test([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])
