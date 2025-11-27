# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]

# Output: 8

# Explanation:

# n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)                       # array ki length
        total = n * (n + 1) // 2            # 0..n tak ka expected sum
        return total - sum(nums)            # missing = expected - actual

        # n = len(nums)
        # for i in range(0,n+1):
        #     if i not in nums:
        #         return i




class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        freq_map = {}

        # Step 1: Initialize dictionary with all numbers from 0 to n
        for i in range(n + 1):
            freq_map[i] = 0

        # Step 2: Mark all present numbers
        for num in nums:
            freq_map[num] = 1

        # Step 3: Find number whose frequency is still 0 (missing)
        for key, value in freq_map.items():
            if value == 0:
                return key

        # Alternate method using only range (same logic):
        # for i in range(n):
        #     freq_map[nums[i]] = 1
        #
        # for i in range(n+1):
        #     if freq_map[i] == 0:
        #         return i
