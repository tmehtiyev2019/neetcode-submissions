class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j =0, 0
        #consider m and n in the imp.
        while i<=len(nums1)-1  and j<=len(nums2)-1:
            if i>= m:
                l = i
                while l<=len(nums1)-1:
                    nums1[l] = nums2[j]
                    l += 1
                    j += 1
                continue
            if nums1[i] <= nums2[j]:
                i += 1
                continue
                # continue checking the next elements in nums1
            if nums1[i] > nums2[j]:
                k=len(nums1)-1
                while k>i:
                    nums1[k]=nums1[k-1]
                    k -= 1
                nums1[i]=nums2[j]
                j += 1
                m += 1



        