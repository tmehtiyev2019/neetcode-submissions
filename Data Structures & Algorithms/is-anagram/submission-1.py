class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag_map={}

        for char in s:
            anag_map[char] = anag_map.get(char,0) + 1
        for char in t:
            anag_map[char] = anag_map.get(char,0) - 1
        for key, val in anag_map.items():
            if val != 0:
                return False
        return True

        #time comp: O(n)
        #space comp: O(n)



        # # if len(s)!=len(t):
        # #     return False
        # s_map={}
        # t_map={}
        # for char in s:
        #     s_map[char]=s_map.get(char,0)+1
        # for char in t:
        #     t_map[char]=t_map.get(char,0)+1
        # return s_map==t_map



# Input: s = "racecar", t = "carrace"

# anag_map={r:0, a:0, c:0}


# Output: true

