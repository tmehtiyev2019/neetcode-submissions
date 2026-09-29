class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s2_map = {}

        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        L = 0
        for R in range(len(s2)):
            s2_map[s2[R]] = s2_map.get(s2[R], 0) + 1
            if R - L + 1 == k:
                if s2_map == s1_map:
                    return True
                s2_map[s2[L]] -= 1
                if s2_map[s2[L]] == 0:
                    del s2_map[s2[L]]
                L += 1
        return False






# # Input: s1 = "abc", s2 = "lecabee"

# # Output: true

#         char_list = list(s1)
#         base_char = char_list.copy()

#         L = 0
#         for R in range(len(s2)):
            
#             if s2[R] in s1:
#                 char_list.remove(s2[R])
#             else:
#                 char_list = base_char.copy()
#                 L = R
#             if len(char_list) == 0:
#                 return True
#         return False
            



        