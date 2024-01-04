
def productExceptSelf(nums):
    answer = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]
    return answer
    

if __name__ == "__main__":
    case1 = [1,2,3,4]
    case2 = [-1, 1, 0, -3, 3]
    cases = [case1, case2]
    expected = [[24,12,8,6], [0,0,9,0,0]]

    for i, exp in enumerate(expected):
        # print(productExceptSelf(cases[i]))
        assert productExceptSelf(cases[i]) == expected[i]
    print('ok')