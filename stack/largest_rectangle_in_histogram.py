def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area
        
if __name__ == "__main__":
    case1 = [2,1,5,6,2,3]
    case2 = [2,4]
    cases = [case1, case2]

    expected = [10, 4]

    for i, exp in enumerate(cases):
        assert(largestRectangleArea(cases[i]) == expected[i])
    print('ok')