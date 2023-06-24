"""
LeetCode 13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/

"""


class Solution:
    def romanToInt(self, s: str) -> int:

        hashMap = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}

        total = 0

        for i in range(len(s)):
            if i < len(s) - 1 and hashMap[s[i]] < hashMap[s[i+1]]:
                total -= hashMap[s[i]]
            else:
                total += hashMap[s[i]]

        return total


def test(s, expected_answer):
    answer = Solution().romanToInt(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test('III', 3)
test('LVIII', 58)
test('MCMXCIV', 1994)
