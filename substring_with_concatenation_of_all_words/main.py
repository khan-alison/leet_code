# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """

#         def dfs(path, remaining_words):
#             if not remaining_words:
#                 combine.append("".join(path))
#                 return
#             for i in range(len(remaining_words)):
#                 dfs(path + [remaining_words[i]],
#                     remaining_words[:i] + remaining_words[i+1:])

#         combine = []
#         result = []
#         dfs([], words)
#         h = len(s)
#         for i in combine:
#             for j in range(h - len(i) + 1):
#                 if s[j: j + len(i)] == i:
#                     if j not in result:
#                         result.append(j)
#         return result

#     def combine_length(self, words):
#         length = 0
#         for i in words:
#             length += len(i)
#         return length
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        print(word_len)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = {}
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    if word in current_count:
                        current_count[word] += 1
                    else:
                        current_count[word] = 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)
                else:
                    current_count.clear()
                    left = right

        return result


s = "barfoothefoobarman"
words = ["foo", "bar"]
solution = Solution()
result = solution.findSubstring(s, words)
print(result)


s, words = "wordgoodgoodgoodbestword",  ["word", "good", "best", "good"]
solution = Solution()
result = solution.findSubstring(s, words)
print(result)
