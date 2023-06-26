"""
LeetCode 13. Roman to Integer

https://leetcode.com/problems/roman-to-integer/

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        ans = 0
        for i in range(len(s)):
            if (i + 1 < len(s) and romanInt[s[i]] < romanInt[s[i+1]]):
                ans -= romanInt[s[i]]
            else:
                ans += romanInt[s[i]]

        return ans


def test(s, expected_answer):
    answer = Solution().romanToInt(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test("III", 3)
test("LVIII", 58)
test("MCMXCIV", 1994)
