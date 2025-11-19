# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Merge function
        def merge_array(left, right):
            res = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:])
            res.extend(right[j:])
            return res

        # Merge Sort function
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge_array(left, right)

        # Sort both strings using merge sort
        sorted_s = merge_sort(list(s))
        sorted_t = merge_sort(list(t))

        return sorted_s == sorted_t
