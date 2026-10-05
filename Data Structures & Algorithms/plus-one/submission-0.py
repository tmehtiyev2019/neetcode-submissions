class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        total = 0
        q = deque()
        cn = 0
        for i in range(len(digits)-1, -1, -1):
            total += digits[i] * 10**cn
            cn += 1
        total += 1

        while total:
            num = total % 10
            q.appendleft(num)
            total = total // 10

        return list(q)



# time comp: O(n)
# space_comp: O(n)



# Dry Run:

# Input: digits = [9,9,9]

# Output: [1,0,0,0]
        