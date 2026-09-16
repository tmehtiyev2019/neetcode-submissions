class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        l = 0
        seen_dict=defaultdict(lambda:-1)
        r=0

        while r<len(s):
            char = s[r]
            # to add a char, it shuold not be in the window, but it could be in the dict
            char_idx = seen_dict[char]
            # if this index is in window, duplicate
            if l <= char_idx:
                max_len=max(max_len,r - l)
                l=seen_dict[char] + 1
                seen_dict[char] = r
            else:
                seen_dict[char] = r
            # if this index is not in window, new char
                
            r+=1
        max_len=max(max_len,r - l)
        return max_len

#abba

# {"x":0,y:1,z:2}

        