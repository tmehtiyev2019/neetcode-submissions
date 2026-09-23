# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_group = defaultdict(list)
#         res = []
#         for a in strs: #time comp: O(n)
#             key = tuple(sorted(a)) # time comp: O(mlogm)
#             anagram_group[key].append(a)
#         for val in anagram_group.values(): #time comp: O(n)
#             res.append(val)
#         return res

#         #time comp: O(mlogm)
#         #space comp: O(n)

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         anagram_group = defaultdict(list)
#         res = []
#         for a in strs: #time comp: O(n)
#             key = tuple(sorted(a)) # time comp: O(mlogm)
#             anagram_group[key].append(a)
#         for val in anagram_group.values(): #time comp: O(n)
#             res.append(val)
#         return res

#         #time comp: O(mlogm)
#         #space comp: O(n)
            


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        res = []
        for a in strs: 
            char_hash = [0] * 26
            for char in a:
                char_hash[ord(char)-ord('a')] += 1
            key = tuple(char_hash) 
            anagram_group[key].append(a)
        for val in anagram_group.values():
            res.append(val)
        return res



























        # hm={}
        # out=[]
        # for item in strs:
        #     if sorted(item) in dict:
        #         dict[sorted(item)].append(item)
        #     else:
        #         dict[sorted(item)]=[]
        #         dict[sorted(item)].append(item)
        # for keys, items in dict.items():
        #     out.append(items)
        # return out





            



        