# 


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicate_set = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                duplicate_set.remove(nums[L])
                L += 1
            if nums[R] in duplicate_set:
                return True
            duplicate_set.add(nums[R])
        return False




        