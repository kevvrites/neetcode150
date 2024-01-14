def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False
    freq1 = [0 for _ in range(26)]
    freq2 = [0 for _ in range(26)]
    for letter in word1:
        freq1[ord(letter) - ord('a')] += 1
    for letter in word2:
        freq2[ord(letter) - ord('a')] += 1
    
    for i in range(26):
        if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
            return False

    freq1.sort()
    freq2.sort()

    for i in range(26):
        if freq1[i] != freq2[i]:
            return False
    return True

if __name__ == "__main__":
    case1 = ["abc", "bca"]
    case2 = ["a", "aa"]
    case3 = ["cabbba", "abbccc"]
    cases = [case1, case2, case3]

    expected = [True, False, True]

    for i, exp in enumerate(cases):
        assert closeStrings(cases[i][0], cases[i][1]) == expected[i]
    print('ok')