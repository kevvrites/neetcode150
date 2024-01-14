def generateParentheses(n):
    stack = []
    ans = []

    def backtrack(open, close):
        if open == close == n:
            ans.append("".join(stack))
            return
        
        if open < n:
            stack.append('(')
            backtrack(open + 1, close)
            stack.pop()
        
        if close < open:
            stack.append(')')
            backtrack(open, close + 1)
            stack.pop()
    
    backtrack(0, 0)
    return ans

if __name__ == "__main__":
    case1 = 3
    case2 = 1
    cases = [case1, case2]

    expected = [["((()))","(()())","(())()","()(())","()()()"], ["()"]]

    for i, exp in enumerate(cases):
        assert generateParentheses(cases[i]) == expected[i]
    print('ok')