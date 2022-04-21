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


def brackets(string):

    closed_list = ["}", "]", ")"]
    opp_elem = ""
    brack_list = []

    if len(string) % 2 != 0:
        return False

    for elem in string:
        if elem not in closed_list:
            brack_list.append(elem)

        else:
            if elem == "}":
                opp_elem = "{"
            if elem == "]":
                opp_elem = "["
            if elem == ")":
                opp_elem = "("

            if brack_list and opp_elem == brack_list[len(brack_list) - 1]:
                del brack_list[-1]

            else:
                return False

    if brack_list.__len__() != 0:
        return False

    return True


print(brackets("()"))
