def two_sum(nums, target):
    seen = {}
    for index, num in enumerate(nums):
        looking_for = target - num
        if looking_for in seen:
            return [seen[looking_for], index]
        else:
            seen[num] = index
    pass

# Test
print(two_sum([2, 7, 11, 15], 9))  # should return [0, 1]
