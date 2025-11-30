# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq_map = {}

        for i in range(n):
            if nums[i] in freq_map:
                freq_map[nums[i]] += 1
            else:
                freq_map[nums[i]] = 1
                
        for key,value in freq_map.items():
            if value == 1:
                return key            

        
        