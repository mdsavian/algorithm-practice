"""
LeetCode 268. Missing Number

https://leetcode.com/problems/missing-number/

"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) not in nums:
            return len(nums)

        for i in range(len(nums)):
            if i not in nums:
                return i


def test(s, expected_answer):
    answer = Solution().missingNumber(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test([3, 0, 1], 2)
test([0, 1], 2)
test([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)
