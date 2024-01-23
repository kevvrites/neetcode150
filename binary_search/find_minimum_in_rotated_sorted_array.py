def findMin(nums):
    ans = 5001
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
           ans = min(ans, nums[l])
           break
 
        m = (l + r) // 2
        ans = min(ans, nums[m])

        if nums[l] > nums[m]:
            r = m - 1
        else:
            l = m + 1
    return ans

if __name__ == "__main__":
    case1 = [3,4,5,1,2]
    case2 = [4,5,6,7,0,1,2]
    case3 = [11,13,15,17]
    case4 = [2,3,1]
    cases = [case1, case2, case3, case4]

    expected = [1,0,11,1]

    for i, exp in enumerate(cases):
        assert(findMin(exp) == expected[i])
    print('ok')