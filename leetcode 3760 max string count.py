# You are given a string s consisting of lowercase English letters.

# Return an integer denoting the maximum number of substrings you can split s into such that each substring starts with a distinct character (i.e., no two substrings start with the same character).

 

# Example 1:

# Input: s = "abab"

# Output: 2

# Explanation:

# Split "abab" into "a" and "bab".
# Each substring starts with a distinct character i.e 'a' and 'b'. Thus, the answer is 2.
# Example 2:

# Input: s = "abcd"

# Output: 4

# Explanation:

# Split "abcd" into "a", "b", "c", and "d".
# Each substring starts with a distinct character. Thus, the answer is 4.
# Example 3:

# Input: s = "aaaa"

# Output: 1

# Explanation:

# All characters in "aaaa" are 'a'.
# Only one substring can start with 'a'. Thus, the answer is 1.

class Solution:
    def maxDistinct(self, s: str) -> int:
        freq = {}
        res = []   # using append to store distinct characters

        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        for key, value in freq.items():
            if value >= 1:       # check distinct characters
                res.append(key) # using append

        return len(res)         # return count of distinct chars
