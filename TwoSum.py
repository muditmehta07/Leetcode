class Solution(object):
    def twoSum(self, nums, target):
        L = {}

        for i, num in enumerate(nums):
            sub = target - num
            if sub in L:
                return [L[sub], i]
            L[num] = i
