# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if n <= 1:
#             return    #[0]

#         i = 0    
#         for j in range(n):
#             if nums[j] != 0:     
#                 nums[i],nums[j] = nums[j],nums[i]    #swapping
#                 i+=1    #increase the value of i

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        temp = []
        

        for i in range(0,n):
            if nums[i] != 0:
                temp.append(nums[i])

        m = len(temp)
        for i in range(0,m):
            nums[i] = temp[i]
        for i in range(m,n):
            nums[i] = 0

                