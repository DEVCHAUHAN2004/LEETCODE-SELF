# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

class Solution(object):
    def thirdMax(self, nums):
        n = len(nums)
        largest = float("-inf")
        s_largest = float("-inf")
        t_largest = float("-inf")

        # If less than 3 unique numbers → return largest
        if len(set(nums)) < 3:
            return max(nums)

        # Find largest
        for i in range(n):
            if nums[i] > largest:
                largest = nums[i]

        # Find second largest (not equal to largest)
        for i in range(n):
            if nums[i] > s_largest and nums[i] != largest:
                s_largest = nums[i]

        # Find third largest (not equal to largest & second largest)
        for i in range(n):
            if nums[i] > t_largest and nums[i] != largest and nums[i] != s_largest:
                t_largest = nums[i]

        return t_largest
