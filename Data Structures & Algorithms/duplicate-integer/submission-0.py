class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # val=set()
        # for i in nums:
        #     if i in val:
        #         return True
        #     val.add(i)
        # return False

        numb_map = {}

        for num in nums:
            if num not in numb_map:
                numb_map[num]=1
            else:
                numb_map[num] += 1
        for key, value in numb_map.items():
            if value>1:
                return True
        return False


        