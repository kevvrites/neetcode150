def halvesAreAlike(s):
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    num1 = 0
    num2 = 0
    def isVowel(letter):
        if letter in ('aeiouAEIOU'):
            return 1
        return 0
    for letter in a:
        num1 += isVowel(letter)
    for letter in b:
        num2 += isVowel(letter)
    if num1 == num2:
        return True
    return False

if __name__ == "__main__":
    case1 = "book"
    case2 = "textbook"
    cases = [case1, case2]

    expected = [True, False]

    for i, exp in enumerate(cases):
        assert halvesAreAlike(cases[i]) == expected[i]
    print('ok')