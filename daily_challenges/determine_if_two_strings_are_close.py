def closeStrings(word1, word2):
    if len(word1) != len(word2):
        return False
    word1 = sorted(word1)
    word2 = sorted(word2)
    diff = []
    count = 0
    for i in range(len(word1)):
        letters = set()
        if word1[i] != word2[i]:
            letters.add(word1[i])
            letters.add(word2[i])
            diff.append(letters)
    letters = set.union(*diff) if diff else []
    if len(letters) > 3:
        return False
    else:
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