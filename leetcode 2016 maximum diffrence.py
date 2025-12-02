# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

# Return the maximum difference. If no such i and j exists, return -1.

 

# Example 1:

# Input: nums = [7,1,5,4]
# Output: 4
# Explanation:
# The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
# Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
# Example 2:

# Input: nums = [9,4,3,2]
# Output: -1
# Explanation:
# There is no i and j such that i < j and nums[i] < nums[j].
# Example 3:

# Input: nums = [1,5,2,10]
# Output: 9
# Explanation:
# The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1  # initially assume no valid answer

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    diff = nums[j] - nums[i]
                    max_diff = max(max_diff, diff)

        return max_diff








class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_val = nums[0]       # Minimum value seen so far
        max_diff = -1           # Initialize max difference

        for i in range(1, n):
            if nums[i] > min_val:
                # Update max difference if current - min_val is bigger
                max_diff = max(max_diff, nums[i] - min_val)
            else:
                # Update min_val if current number is smaller
                min_val = nums[i]

        return max_diff
