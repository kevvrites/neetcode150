def containsDuplicate(nums):
    setNums = set()
    for num in nums:
        if num in setNums:
            return True
        setNums.add(num)
    return False
