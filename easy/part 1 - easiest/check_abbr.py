"""408 Valid Word Abbreviation"""

# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
# A string such as "word" contains only the following valid abbreviations:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word".
# Any other string is not a valid abbreviation of "word".
# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
# Return true.
# Example 2:
# Given s = "apple", abbr = "a2e":
# Return false.


def check_abbr(string, abbr):

    i = 0
    j = 0

    if len(abbr) > len(string):
        return False

    while i < len(string):
        if j >= len(abbr):
            return False

        if string[i] == abbr[j]:
            i += 1
            j += 1
            continue

        elif abbr[j].isalpha():
            return False

        else:
            num = 0
            while len(abbr) - j - 1 > 0 and abbr[j+1].isdigit():
                num += int(abbr[j]) * 10
                j += 1

            num += int(abbr[j])

            if num > len(string):
                return False
            i += num
            j += 1
            print(i)
            print(j)

    return True


boolean = check_abbr("word", "1o1d")

print(boolean)
