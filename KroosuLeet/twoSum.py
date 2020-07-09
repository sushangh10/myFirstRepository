class Solution:
    def __init__(self):
        pass

    def twoSum1(self, nums, target):
        """通过	6812 ms	14.6 MB	Python3 """
        for i in range(len(nums)):
            j_list = nums[i+1:]
            for j in range(len(j_list)):
                if nums[i] + j_list[j] == target:
                    return [i, i+j+1]

    def twoSum2(self, nums, target):
        """通过	1184 ms	14.6 MB	Python3"""
        for i in range(len(nums)):
            if (target - nums[i]) in nums:
                if i == nums.index(target - nums[i]):
                    continue
                else:
                    return [i, nums.index(target-nums[i])]
            else:
                continue

    def twoSum3(self, nums, target):
        """通过	60 ms	15.2 MB	Python3"""
        temp_dict = dict()
        for k, v in enumerate(nums):
            if target - v in temp_dict:
                return [temp_dict[target-v], k]
            temp_dict[v] = k
