class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)
        res = []
        for a in strs:
            key = tuple(sorted(a)) 
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





            



        