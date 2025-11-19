# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def merge(left, right):
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i < len(left):
                res.extend(left[i:])
            if j < len(right):
                res.extend(right[j:])
            return res

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        sorted_nums = merge_sort(nums)
        nums[:] = sorted_nums  # in-place update


# ----------- Testing code (VS Code run) ----------------
nums = [2, 0, 2, 1, 1, 0]
print("Original nums:", nums)

solution = Solution()
solution.sortColors(nums)

print("Sorted nums:  ", nums)
