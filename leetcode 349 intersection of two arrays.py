# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
class Solution:
    def intersection(self, nums1,nums2):
        x = set(nums1)
        y = set(nums2)

        result = x & y

        return list(result)
    



class Solution(object):
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()

        i = j = 0
        res = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if nums1[i] not in res:   # 👉 Simple duplicate check
                    res.append(nums1[i])
                i += 1
                j += 1

        return res
