class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sum_array=len(nums)*[0]
        k_diff_map = {0:1} 

        #cumulative sum
        for i in range(len(nums)):
            cum_sum += nums[i]
            sum_array[i] = cum_sum

        #lookig for the diff with k
        for i in range(len(sum_array)):
            diff = sum_array[i] - k
            if diff in k_diff_map:
                count += k_diff_map[diff]
            k_diff_map[sum_array[i]] = k_diff_map.get(sum_array[i], 0) + 1

        return count


        
        

# question: how to initalize a map with value as list
#sum_array=len(nums)*[0] what are the other eays to initialize it?




# Input: nums = [2,-1,1,2], k = 2


# cum_sum_nums = [2,1,2,4]


# {0:1, 2:1, 1: 1, }

# 2 --> count 2

# {0:1, 2:2, 1: 1, }

# 4 --> the diff is 2 --> val of 2 in map -->2

# count += k_diff_map[diff] -->4

# {0:1, 2:2, 1: 1, 4:1 }



# goal: is to find the subtraction where the differece is k
# we start with two pointers
# i  both starts with index 0
# i = 0
# nums[i]-->2
# add 2 to hashmap-->{2:0}

# next

# i = 1
# nums[i]-->1
# check if k(2)-1=1 in the map if yes get the vlaue (index j) and the current index i --> result nums[j:i+1]
# we add 1 to the map {2:[0,2], 1:[1], 4:[3]}
# add 2 to set-->






# subarray size in range(1, len(nums))
# 1: easy
# 2: easy

# Output: 4





# subarray[1 len(nums)]

# Input: nums = [2,-1,1,2], k = 2
# [2,1,2,4]



# [1, 2, 3] k=3
# [1,3,6]

# total=sum(nums)=4


# count=0
# for i in nums:
#     if total-i=k:
#         count += 1

# i was the individual sum
# what is we can also get the gorup sum
# gorup size can start form 2 to all the way up to the len(nums)
# grouping will be comp heavy?


# sort:

# [-1,1,2,2] k=2

# i=0
# j=len(nums)-1

# if j > k


# if -1 < k:


# group size in range (1, len(nums))









        