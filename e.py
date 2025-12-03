nums = [1,7,4,9,2,5]
def wiggleMaxLength(nums):
        n = len(nums)
        res = []

        for i in range(0,n):
            nums[i-1] -= nums[i]
            res.append(nums[i-1])
        return res

print(wiggleMaxLength(nums))