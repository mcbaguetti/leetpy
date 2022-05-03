"""20. Valid Parentheses"""

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([]{})"
# Output: true

# Example 5:
# Input: s = ")("
# Output: false

# Example 6:
# Input: s = "(}){"
# Output: false

# Ex 7:
# "([)]"
# false


def brackets(s):

    closed_list = {"}": "{", "]": "[", ")": "("}
    brack_list = []
    bracket_dict = {"}": "{", "]": "[", ")": "("}  # closed_bracket: open_bracket
    stack = []

    for elem in s:
        if elem not in bracket_dict:
            stack.append(elem)

        else:
            opp_elem = bracket_dict[elem]
            if stack and opp_elem == stack[-1]:
                del stack[-1]
            else:
                return False

    if stack:
        return False

    return True


print(brackets("([)]"))
