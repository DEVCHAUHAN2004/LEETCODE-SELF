# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 🚀 Optimal Solution: In-place rotation using Reverse Method
        # ⏱️ Time: O(n)   💾 Space: O(1)

        n = len(nums)
        k = k % n   # ✨ Handles large k values

        # 🔁 Reverse helper function
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(n-k, n-1)   # 🔄 Step 1: Reverse last k elements
        reverse(0, n-k-1)   # 🔄 Step 2: Reverse first n-k elements
        reverse(0, n-1)     # 🔄 Step 3: Reverse entire array
