def valid_brackets(s):

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
