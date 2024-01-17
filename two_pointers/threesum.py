def threeSum(nums):
    ans = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            if a + nums[l] + nums[r] > 0:
                r -= 1
            elif a + nums[l] + nums[r] < 0:
                l += 1
            else:
                ans.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return ans

if __name__ == "__main__":
    case1 = [-1,0,1,2,-1,-4]
    case2 = [0,1,1]
    case3 = [0,0,0]
    cases = [case1, case2, case3]

    exp1 = [[-1,-1,2],[-1,0,1]]
    exp2 = []
    exp3 = [[0,0,0]]
    expected = [exp1, exp2, exp3]

    for i, exp in enumerate(cases):
        assert(threeSum(cases[i]) == expected[i])
    print('ok')
