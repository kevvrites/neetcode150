def isAnagram(s, t):
    return sorted(s) == sorted(t)

if __name__ == '__main__':
    case1 = ['anagram', 'nagaram']
    case2 = ['rat', 'car']
    cases = [case1, case2]

    expected = [True, False]
    
    for i, exp in enumerate(expected):
        assert isAnagram(cases[i][0], cases[i][1]) == expected[i]
    print('ok')