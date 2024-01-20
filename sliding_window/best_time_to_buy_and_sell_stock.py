def buy_and_sell(prices):
    l = 0
    r = 1
    max_profit = 0
    
    if len(prices) == 1:
        return 0
    
    while r <= len(prices):
        if prices(l) > prices(r):
            l = r
            r = l + 1
        if prices(r) >= prices(l):
            profit = prices(r) - prices(l)
            max_profit = max(max_profit, profit)
            r += 1
    return max_profit 

if __name__ == "__main__":
    case1 = [7,1,5,3,6,4]
    case2 = [7,6,4,3,1]
    cases = [case1, case2]
    
    expected = [5,0]
    
    for i, exp in enumerate(cases):
        assert(buy_and_sell(exp) == expected[i])
    print("ok") 