"""
LeetCode 169. Majority Element

https://leetcode.com/problems/majority-element/

"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
            if hashMap[i] > len(nums) // 2:
                return i


def test(s, expected_answer):
    answer = Solution().majorityElement(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test([3, 2, 3], 3)
test([2, 2, 1, 1, 1, 2, 2], 2)
