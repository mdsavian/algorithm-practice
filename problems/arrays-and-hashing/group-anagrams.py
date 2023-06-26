"""
LeetCode 49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

"""

from typing import List


# para cada string eu transformo ela em um hash
# ai eu vou poder comparar se cada hash eh igual, se for eu adiciono em um array que sera adicionado na resposta
# o problema eh q pra cada string q eu ler vai ser On^2

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = []
        hashStrings = {}

        # create hashmap for each string On^2
        for s in strs:
            hashWord = {}
            for j in s:
                hashWord[j] = 1 + hashStrings.get(j, 0)

            hashStrings[s] = hashWord

        # agora a ideia seria pegar cada hash e comparar o objeto dentro dele com outro
        # for hash in hashStrings:

        # brute force
        # for i, s in enumerate(strs):

        #     val = [s]

        #     for j in range(j+1, len(strs)):

        #         print(s, i)

        #     ans.append([s])
        return ans


def test(s, expected_answer):
    answer = Solution().groupAnagrams(s)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}")


test(["eat", "tea", "tan", "ate", "nat", "bat"], [
     ["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
test([""], [[""]])
test(["a"], [["a"]])
