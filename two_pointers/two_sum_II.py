def twoSum(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            return [l + 1, r + 1]

if __name__ == "__main__":
    case1 = [[2,7,11,15], 9]
    case2 = [[2,3,4], 6]
    case3 = [[-1,0], -1]
    cases = [case1, case2, case3]

    exp1 = [1,2]
    exp2 = [1,3]
    exp3 = [1,2]
    expected = [exp1, exp2, exp3]

    for i, exp in enumerate(cases):
        assert(twoSum(cases[i][0], cases[i][1]) == expected[i])
    print('ok')
