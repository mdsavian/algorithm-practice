"""
58. Length of Last Word

https://leetcode.com/problems/length-of-last-word/

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for c in s[::-1]:
            if c != " ":
                length += 1
            else:
                if length > 0:
                    return length

        return length


def test(s, expected_answer):
    answer = Solution().lengthOfLastWord(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test("a", 1)
test("Hello World", 5)
test("   fly me   to   the moon  ", 4)
test("luffy is still joyboy", 6)
test("Today is a nice day", 3)
