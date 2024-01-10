def isValid(s):
    buf = []
    open = '([{'
    lookup_table = {')':'(', ']':'[', '}':'{'}
    for letter in s:
        if letter in lookup_table:
            if buf and buf[-1] == lookup_table[letter]:
                buf.pop()
            else:
                return False
        else:
            buf.append(letter)
    return True if not buf else False

if __name__ == "__main__":
    case1 = "()"
    case2 = "()[]{}"
    case3 = "(]"
    cases = [case1, case2, case3]
    
    expected = [True, True, False]
    
    for i, exp in enumerate(cases):
        assert isValid(cases[i]) == expected[i]
    print("ok")
        
