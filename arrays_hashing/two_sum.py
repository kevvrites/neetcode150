def twoSum(nums, target):
    table = {}
    for i in range(len(nums)):
        if target - nums[i] in table:
            return [i, table[target - nums[i]]]
        else:
            table[nums[i]] = i

if __name__ == '__main__':
    case1 = ([2,7,11,15], 9)
    case2 = ([3,2,4], 6)
    case3 = ([3,3], 6)
    cases = [case1, case2, case3]

    expected = [[0,1], [1,2], [0,1]]
    
    for i, exp in enumerate(expected):
        assert sorted(twoSum(cases[i][0], cases[i][1])) == expected[i]
    print('ok')