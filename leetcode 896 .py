# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

# Example 1:

# Input: nums = [1,2,2,3]
# Output: true
# Example 2:

# Input: nums = [6,5,4,4]
# Output: true
# Example 3:

# Input: nums = [1,3,2]
# Output: false

class Solution(object):
    def isMonotonic(self, nums):
        n = len(nums)
        inc = True   # assume non-decreasing
        dec = True   # assume non-increasing

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                inc = False
            if nums[i] < nums[i+1]:
                dec = False

        return inc or dec
