# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3

class Solution:
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        freq_map = {}

        for i in range(0,n):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1

        for key,value in freq_map.items():  
            if value >= 2:
                return key              
            


class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

