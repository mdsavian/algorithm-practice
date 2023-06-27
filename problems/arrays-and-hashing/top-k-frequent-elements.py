"""

347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashNums = {}

        # O(n)
        for i in nums:
            hashNums[i] = 1 + hashNums.get(i, 0)

        # O(n log n)
        sortHash = dict(
            sorted(hashNums.items(), key=lambda x: x[1], reverse=True))

        answ = []

        # O(n)
        for i in range(k):
            answ.append(list(sortHash.keys())[i])

        return answ


def test(s, t, expected_answer):
    answer = Solution().topKFrequent(s, t)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test([1, 1, 2, 2, 2, 3, 3, 3], 2, [2, 3])
test([1, 1, 1, 2, 2, 3], 2, [1, 2])
test([1], 1, [1])
