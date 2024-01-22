def searchMatrix(matrix, target):
    l, r = 0, len(matrix) - 1
    low, high = 0, len(matrix[0])
    while l <= r:
        mid = (l+r) // 2
        if matrix[mid][0] <= target and matrix[mid][-1] >= target:
            col = matrix[mid]
            while low <= high:
                mid = (low + high) // 2
                if col[mid] == target:
                    return True
                elif col[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return False
        elif matrix[mid][0] > target:
            r = mid - 1
        else:
            l = mid + 1


if __name__ == "__main__":
    case1 = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3]
    case2 = [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13]
    cases = [case1, case2]

    expected = [True, False]

    for i, exp in enumerate(cases):
        assert(searchMatrix(exp[0], exp[1]) == expected[i])
    print('ok')