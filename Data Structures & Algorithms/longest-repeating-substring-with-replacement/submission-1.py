
# Brute Force Approach
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res = 0

#         for i in range(len(s)):
#             char_count = {}
#             max_char = 0
#             for j in range(i, len(s)):
#                 char_count[s[j]] = char_count.get(s[j], 0) + 1
#                 max_char = max(max_char, char_count[s[j]])
#                 if j - i + 1 - max_char <= k:
#                     res = max(res,j - i + 1)
#         return res



# Sliding Window
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        L = 0
        char_count = {}
        max_char = 0
        for R in range(len(s)):
            char_count[s[R]] = char_count.get(s[R], 0) + 1
            while R - L + 1 - max(char_count.values()) > k:
                char_count[s[L]] -= 1
                L += 1
            res = max(res, R - L + 1)
                    # make sure max_char is updated
        return res








        # rep_char = 0
        # char = a
        

        # for c in range(1, len(s)):
        #     if str[i] == str[i-1]:
        #         rep_char += 1
        #     else:
        #         rep_char = 0
                
        # return rep_char


# Input: s = "XYYX", k = 2









# Output: 4

# frist find the longest repating characters

# Steps:
# 1. To find the longest repeating character lenght in s by considereing the k buffer
# 2. To add 2 more -- the issue is by replacing other s tow longest repeating characters which were collased by yhr other char might merge and create a new one
        