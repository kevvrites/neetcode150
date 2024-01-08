def longestConsecutive(nums):
    table = set(nums)
    max_seq = 0
    for num in nums:
        if num - 1 not in table:
            seq = 0
            while num + seq in table:
                seq += 1
            if seq > max_seq:
                max_seq = seq
    return max_seq

if __name__ == '__main__':
    case1 = [100,4,200,1,3,2]
    case2 = [0,3,7,2,5,8,4,6,0,1]
    cases = [case1, case2]

    expected = [4, 9]
    for i, exp in enumerate(expected):
        assert(longestConsecutive(cases[i]) == expected[i])
    print('ok')