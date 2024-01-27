def lengthOfLongestSubstring(s):
        l = 0
        length = 0
        substring = set()
    
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            length = max(length, r - l + 1)
        return length

if __name__ == "__main__":
    case1 = "abcabcbb"
    case2 = "bbbbb"
    case3 = "pwwkew"
    cases = [case1, case2, case3]
    expected = [3,1,3]
    
    for i, exp in enumerate(cases):
        assert(lengthOfLongestSubstring(exp) == expected[i])
    print("ok") 