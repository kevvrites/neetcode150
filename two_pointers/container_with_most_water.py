def maxArea(height):
    l = 0
    r = len(height) - 1
    areas = []
    while l < r:
        x = r - l
        if height[r] >= height[l]:
            y = height[l]
            l += 1
        else:
            y = height[r]
            r -= 1
        areas.append(x * y)
    return max(areas)

if __name__ == "__main__":
    case1 = [1,8,6,2,5,4,8,3,7]
    case2 = [1,1]
    cases = [case1, case2]

    expected = [49, 1]

    for i, exp in enumerate(cases):
        assert(maxArea(cases[i]) == expected[i])
    print('ok')
