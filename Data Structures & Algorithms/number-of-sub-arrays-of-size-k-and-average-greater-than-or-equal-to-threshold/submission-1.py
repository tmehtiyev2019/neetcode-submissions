class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarr_count = 0

        #edge cases
        if len(arr) <= k:
            return 1 if sum(arr) / len(arr) >= threshold else 0

        for i in range(len(arr) - k + 1):
            curr_avg = 0
            for j in range(i , i + k):
                curr_avg += arr[j]
            if curr_avg / k >= threshold:
                subarr_count += 1
        return subarr_count

        