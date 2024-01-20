def search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2
        if target == nums[mid]:
            return mid
        
        elif target > nums[mid]:
            start = mid + 1

        elif target < nums[mid]:
            end = mid - 1
        
    return -1

if __name__ == "__main__":
    case1 = [[-1,0,3,5,9,12], 9]
    case2 = [[-1,0,3,5,9,12], 2]
    cases = [case1, case2]
    expected = [4, -1]

    for i, exp in enumerate(cases):
        assert(search(exp[0], exp[1]) == expected[i])
    print('ok')