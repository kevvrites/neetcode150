def encode(arr):
    encoded = ''
    for word in arr:
        encoded += str(len(word)) + '!' + word
    return encoded

def decode(str):
    original = []
    start = 0

    while start < len(str):
        ptr = start
        while str[ptr] != '!':
            ptr += 1
        length = int(str[start:ptr])
        original.append(str[ptr + 1: ptr + 1 + length])
        start = ptr + 1 + length
    return original


if __name__ == "__main__":
    case1 = ['hello','world']
    case2 = ['goodbye', 'cheerio']
    cases = [case1, case2]

    expected = [case1, case2]
    for i, exp in enumerate(cases):
        assert(decode(encode(cases[i])) == expected[i])
    print('ok')
