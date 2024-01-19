def trap(height):
    trapped = 0
    l = 0
    r = len(height) - 1
    max_l = height[l]
    max_r = height[r]
    while l < r:
        if max_l <= max_r:
            l += 1
            max_l = max(max_l, height[l])
            trapped += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            trapped += max_r - height[r]

    return trapped

if __name__ == "__main__":
    case1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    case2 = [4,2,0,3,2,5]
    cases = [case1, case2]

    expected = [6, 9]

    for i, exp in enumerate(cases):
        assert(trap(cases[i]) == expected[i])
    print('ok')