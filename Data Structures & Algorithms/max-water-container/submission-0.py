class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_point=0
        right_point=len(height)-1
        max_amount=0

        while left_point< right_point:
            current_amount=min(height[left_point],height[right_point])*(right_point-left_point)
            max_amount=max(max_amount,current_amount)

            if height[left_point]<=height[right_point]:
                left_point+=1
            else:
                right_point-=1  
        return max_amount