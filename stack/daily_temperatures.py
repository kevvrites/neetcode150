def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    temp_stack = []

    for i, t in enumerate(temperatures):
        while temp_stack and t > temp_stack[-1][0]:
            temp, index = temp_stack.pop()
            answer[index] = (i - index)
        temp_stack.append([t, i])
    return answer

if __name__ == "__main__":
    case1 = [73,74,75,71,69,72,76,73]
    case2 = [30,40,50,60]
    case3 = [30,60,90]
    cases = [case1, case2, case3]

    exp1 = [1,1,4,2,1,1,0,0]
    exp2 = [1,1,1,0]
    exp3 = [1,1,0]
    expected = [exp1, exp2, exp3]
    
    for i, exp in enumerate(cases):
        assert dailyTemperatures(cases[i]) == expected[i]
    print('ok')