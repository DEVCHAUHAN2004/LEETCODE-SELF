# # Given an array of integers nums, sort the array in ascending order and return it.

# # You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

# # Example 1:

# # Input: nums = [5,2,3,1]
# # Output: [1,2,3,5]
# # Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# # Example 2:

# # Input: nums = [5,1,1,2,0,0]
# # Output: [0,0,1,1,2,5]
# # Explanation: Note that the values of nums are not necessarily unique.
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
        
#         def merge_sort(arr):
#             if len(arr) <= 1:
#                 return arr
            
#             mid = len(arr) // 2
#             left = merge_sort(arr[:mid])
#             right = merge_sort(arr[mid:])
            
#             return merge(left, right)

#         def merge(left, right):
#             merged = []
#             i = j = 0

#             while i < len(left) and j < len(right):
#                 if left[i] <= right[j]:
#                     merged.append(left[i])
#                     i += 1
#                 else:
#                     merged.append(right[j])
#                     j += 1

#             merged.extend(left[i:])
#             merged.extend(right[j:])
#             return merged

#         return merge_sort(nums)
 