# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

# Example 1:

# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1]
# Output: [1,2]
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        freq_map = {}

        for i in range(1,n+1):
            freq_map[i] = 0

        for num in nums:
            freq_map[num] += 1

        for key,value in freq_map.items():
            if value == 2:
                duplicate = key
            if value == 0:
                missing = key
        return [duplicate,missing]            
        