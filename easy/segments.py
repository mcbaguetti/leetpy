"""434. Number of Segments in a String

Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1


Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '."""


def num_segments(string):

    space = " "
    count = 0
    first_word = False
    str_length = string.__len__()

    if string is None or string == space:
        return 0

    for i, character in enumerate(string):

        if string[i] == space:
            continue

        elif first_word:
            count += 1
            first_word = True

        elif i != str_length - 1 and string[i+1] == space or i == str_length - 1:
            count += 1

    return count


res = num_segments("          ciao c       ia     o                      ")
print(res)
