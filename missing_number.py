def find_missing(nums: list[int]) -> int:
    n = len(nums)
    summed_numbers = sum(range(n + 1))
    missing = summed_numbers - sum(nums)
    return missing

# Test cases:
print(find_missing([3, 0, 1]))        # => 2
print(find_missing([0, 1]))           # => 2
print(find_missing([9,6,4,2,3,5,7,0,1]))  # => 8
