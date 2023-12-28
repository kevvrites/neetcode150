# def topKFrequent(nums, k):
#     table = {}
#     top = []
#     for i in range(len(nums)):
#         if nums[i] in table:
#             table[nums[i]] += 1
#         else:
#             table[nums[i]] = 1
#     for j in range(k):
#         top.append(sorted(table.items(), key=lambda item: item[1], reverse=True)[j][0])
#     return top

def topKFrequent(nums, k):
    table = {}
    freq = [[] for i in range(len(nums) + 1)]
    top = []

    for n in nums:
        table[n] = 1 + table.get(n, 0)
    for n, c in table.items():
        freq[c].append(n)
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            top.append(n)
            if len(top) == k:
                return top

if __name__ == '__main__':
    case1 = ([1,1,1,2,2,3], 2)
    case2 = ([1], 1)
    case3 = ([4,1,-1,2,-1,2,3], 2)
    cases = [case1, case2, case3]
    expected = [[1,2], [1], [-1, 2]]

    for i, exp in enumerate(expected):
        assert sorted(topKFrequent(cases[i][0], cases[i][1])) == expected[i]
    print('ok')