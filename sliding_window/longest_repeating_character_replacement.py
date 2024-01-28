def characterReplacement(s, k):
    l = 0
    count = {}
    maxf = 0
    ans = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        ans = max(ans, r - l + 1)
    return ans

if __name__ == "__main__":
    case1 = ["ABAB", 2]
    case2 = ["AABABBA", 1]
    cases = [case1, case2]

    expected = [4, 4]

    for i, exp in enumerate(cases):
        assert(characterReplacement(exp[0], exp[1]) == expected[i])
    print('ok')