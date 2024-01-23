def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1

if __name__ == "__main__":
    case1 = [[4,5,6,7,0,1,2], 0]
    case2 = [[4,5,6,7,0,1,2], 3]
    case3 = [[1], 0]

    cases = [case1, case2, case3]
    
    expected = [4, -1, -1]

    for i, exp in enumerate(cases):
        assert(search(exp[0], exp[1]) == expected[i])
    print('ok')