def evalRPN(tokens):
    nums = []
    for token in tokens:
        if token not in '+*/-':
            nums.append(int(token))
        else:
            if token == '+':
                val = (nums[-2] + nums[-1])
            elif token == '-':
                val = (nums[-2] - nums[-1])
            elif token == '*':
                val = (nums[-2] * nums[-1])
            elif token == '/':
                val = (int(nums[-2] / nums[-1]))
            nums.pop()
            nums.pop()
            nums.append(val)
    return nums[0]
if __name__ == "__main__":
    case1 = ["2", "1", "+", "3", "*"]
    case2 = ["4","13","5","/","+"]
    case3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    cases = [case1, case2, case3]

    expected = [9, 6, 22]
    
    for i, exp in enumerate(cases):
        assert evalRPN(cases[i]) == expected[i]
    print('ok')