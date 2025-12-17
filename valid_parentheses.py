def is_valid(s: str) -> bool:
    stack = []
    matches = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for e in s:
        if e in matches.values():
            stack.append(e)
        else:
            if len(stack) == 0:
                stack.append(e)
                break
            elif stack[-1] == matches[e]:
                stack.pop()
            else:
                stack.append(e)

    return not bool(stack)

# Test cases:
print(is_valid("()"))        # => True
print(is_valid("()[]{}"))    # => True
print(is_valid("(]"))        # => False
print(is_valid("([)]"))      # => False
print(is_valid("{[]}"))      # => True
print(is_valid(""))          # => True
