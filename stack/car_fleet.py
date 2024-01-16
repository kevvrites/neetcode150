def carFleet(target, position, speed):
    cars = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in sorted(cars)[::-1]:
        stack.append((target - p) / s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)

if __name__ == "__main__":
    case1 = [12, [10,8,0,5,3], [2,4,1,1,3]]
    case2 = [10, [3], [3]]
    case3 = [100, [0,2,4], [4,2,1]]
    cases = [case1, case2, case3]
    
    expected = [3, 1, 1]

    for i, exp in enumerate(cases):
        assert(carFleet(cases[i][0], cases[i][1], cases[i][2]) == expected[i])
    print('ok')