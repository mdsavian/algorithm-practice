"""
LeetCode 268. Missing Number

https://leetcode.com/problems/missing-number/

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        totalLen = 0

        for i, val in enumerate(nums):
            total += val
            totalLen += i + 1

        return totalLen - total


def test(s, expected_answer):
    answer = Solution().missingNumber(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test([3, 0, 1], 2)
test([0, 1], 2)
test([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
