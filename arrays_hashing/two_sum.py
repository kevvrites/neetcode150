def twoSum(nums, target):
    table = {}
    for i in range(len(nums)):
        if target - nums[i] in table:
            return i, table[target - nums[i]]
        else:
            table[nums[i]] = i
