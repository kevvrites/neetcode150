def checkInclusion(s1, s2):
    s1_table = [0] * 26
    s2_table = [0] * 26
    matches = 0
    l = 0

    if len(s1) > len(s2):
        return False
    
    for i in range(len(s1)):
        s1_table[ord(s1[i]) - ord('a')] += 1
        s2_table[ord(s2[i]) - ord('a')] += 1
    
    for i in range(26):
        matches += (1 if s1_table[i] == s2_table[i] else 0)

    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True
        
        index = ord(s2[r]) - ord('a')
        s2_table[index] += 1
        if s1_table[index] == s2_table[index]:
            matches += 1
        elif s1_table[index] + 1 == s2_table[index]:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        s2_table[index] -= 1
        if s1_table[index] == s2_table[index]:
            matches += 1
        elif s1_table[index] - 1 == s2_table[index]:
            matches -= 1
        l += 1

    return matches == 26

if __name__ == "__main__":
    case1 = ["ab", "eidbaooo"]
    case2 = ["ab", "eidboaoo"]
    case3 = ["abc", "bbbca"]
    cases = [case1, case2, case3]

    expected = [True, False, True]

    for i, exp in enumerate(cases):
        assert(checkInclusion(exp[0], exp[1]) == expected[i])
    print('ok')

