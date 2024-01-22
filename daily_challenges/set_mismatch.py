def findErrorNums(nums):
    exp = int((len(nums) * (len(nums) + 1)) / 2)
    num_sum = 0
    unique_sum = 0
    s = set()

    for n in nums:
        num_sum += int(n)
        s.add(n)

    for n in s:
        unique_sum += n

    diff = num_sum - unique_sum
    dupe = exp - unique_sum

    return [diff, dupe]

if __name__ == "__main__":
    case1 = [1,2,2,4]
    case2 = [1,1]
    cases = [case1, case2]

    expected = [[2,3],[1,2]]

    for i, exp in enumerate(cases):
        assert(findErrorNums(exp) == expected[i])
    print('ok')