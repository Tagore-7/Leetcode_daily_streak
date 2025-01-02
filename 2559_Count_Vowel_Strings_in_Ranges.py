#You are given a 0-indexed array of strings words and a 2D array of integers queries.
#
#Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
#
#Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
#
#Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
#
# 
#
#Example 1:
#
#Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
#Output: [2,3,0]
#Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
#The answer to the query [0,2] is 2 (strings "aba" and "ece").
#to query [1,4] is 3 (strings "ece", "aa", "e").
#to query [1,1] is 0.
#We return [2,3,0].
#Example 2:
#
#Input: words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]
#Output: [3,2,1]
#Explanation: Every string satisfies the conditions, so we return [3,2,1].
# 
#
#Constraints:
#
#1 <= words.length <= 105
#1 <= words[i].length <= 40
#words[i] consists only of lowercase English letters.
#sum(words[i].length) <= 3 * 105
#1 <= queries.length <= 105
#0 <= li <= ri < words.length
#
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixsum = [0] * (len(words) + 1)
        vowel_set = set("aeiou")
        prevsum = 0

        for i, word in enumerate(words):
            if word[0] in vowel_set and word[-1] in vowel_set:
                prevsum += 1

            prefixsum[i + 1] = prevsum

        res = [0] * len(queries)

        for i, (l, r) in enumerate(queries):
            res[i] = prefixsum[r + 1] - prefixsum[l]

        return res






        # wordcount = [0] * len(words)
        # vowels = ('a', 'e', 'i', 'o', 'u')

        # if words[0][0] in vowels and words[0][-1] in vowels:
        #     wordcount[0] += 1

        # for i in range(len(words)):
        #     if i and i < len(words):
        #         word = words[i]
        #         if word[0] in vowels and word[-1] in vowels:
        #             wordcount[i] += 1


        # res = [0] * len(queries)

        # print(wordcount)
        #for i, (l, r) in enumerate(queries):
         #   res[i] = sum(wordcount[l: r + 1])

        #return res


        # count = [0] * len(queries)
        # vowels = ('a', 'e', 'i', 'o', 'u')

        # for i, (src, dest) in enumerate(queries):
        #     for j in range(src, dest + 1):
        #         word = words[j]
        #         if word[0] in vowels and word[-1] in vowels:
        #             count[i] += 1
        # return count


