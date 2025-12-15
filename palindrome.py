def is_palindrome(s):
    s = s.lower().replace(" ", "")
    reversed = s[::-1]
    return reversed == s

# Tests
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True
