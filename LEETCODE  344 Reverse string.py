# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# ✅ Reverse a list in-place using the optimal two-pointer method

def reverseArray(nums):
    # initialize two pointers
    left = 0
    right = len(nums) - 1

    # loop until both pointers meet
    while left < right:
        # swap the elements
        nums[left], nums[right] = nums[right], nums[left]
        
        # move pointers toward the center
        left += 1
        right -= 1

    # return the reversed list (optional, since nums changes in-place)
    return nums


# 🔹 Example list
nums = [5, 7, 3, 2, 6, 1, 5, 9, 8]

# call the function
reverseArray(nums)

# print result
print("Reversed List:", nums)
