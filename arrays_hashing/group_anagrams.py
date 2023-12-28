import collections

def groupAnagrams(strs):
    groups = collections.defaultdict(list)
    for i in range(len(strs)):
        key = ''.join(sorted(strs[i]))
        groups[key].append(strs[i])
    return list(groups.values())

if __name__ == '__main__':
    case1 = ["eat","tea","tan","ate","nat","bat"]
    case2 = [""]
    case3 = ["a"]
    cases = [case1, case2, case3]

    expected = ([["eat","tea","ate"],["tan","nat"],["bat"]], [[""]], [["a"]])

    for i, exp in enumerate(expected):
        assert groupAnagrams(cases[i]) == expected[i]
    print('ok')