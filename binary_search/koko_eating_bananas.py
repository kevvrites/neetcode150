import math

def minEatingSpeed(piles, h):
    min_k = 1
    max_k = max(piles)
    ans = max_k

    if len(piles) == h:
        return max_k
    
    while min_k <= max_k:
        
        time = 0
        mid_k = (min_k + max_k) // 2
        
        for i in piles:
            time += math.ceil(i/mid_k)
        
        if time <= h:
            ans = min(ans, mid_k)
            max_k = mid_k - 1
        else:
            min_k = mid_k + 1
    return ans
        
if __name__ == "__main__":
    case1 = [[3,6,7,11], 8]
    case2 = [[30,11,23,4,20], 5]
    case3 = [[30,11,23,4,20], 6]
    case4 = [[10], 9]
    case5 = [[1,1,1,999999999], 10]
    cases = [case1, case2, case3, case4, case5]

    expected = [4, 30, 23, 2, 142857143]
    
    for i, exp in enumerate(cases):
        assert(minEatingSpeed(exp[0], exp[1]) == expected[i])
    print('ok')