def groupAnagrams(strs):
    groups = defaultdict(list)
    for i in range(len(strs)):
        key = ''.join(sorted(strs[i]))
        groups[key].append(strs[i])
    return list(groups.values())
