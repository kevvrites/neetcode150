def isPalindrome(s):
    s = [_ for _ in s.lower() if _ in 'abcdefghijklmnopqrstuvwxyz0123456789']
    s = ''.join(s)
    r = len(s) - 1

    if len(s) <= 1:
        return True
    
    for l in range(len(s) // 2):
        if s[l] != s[r]:
            return False
        r -= 1
    return True

if __name__ == "__main__":
    case1 = "A man, a plan, a canal: Panama"
    case2 = "race a car"
    case3 = " "
    cases = [case1, case2, case3]

    expected = [True, False, True]

    for i, exp in enumerate(cases):
        assert(isPalindrome(cases[i]) == expected[i])
    print('ok')