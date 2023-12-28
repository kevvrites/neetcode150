def containsDuplicate(nums):
    setNums = set()
    for num in nums:
        if num in setNums:
            return True
        setNums.add(num)
    return False



if __name__ == '__main__':
    case1 = [1,2,3,1]
    case2 = [1,2,3,4]
    case3 = [1,1,1,3,3,4,3,2,4,2]
    cases = [case1, case2, case3]

    expected = (True, False, True)

    for i, exp in enumerate(expected):
        assert containsDuplicate(cases[i]) == expected[i]
    print('ok')
