"""659 · Encode and Decode Strings

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

Example
Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s

    return res


def decode(str):
    strs = []
    i = 0

    while i < len(str):
        j = i

        while str[j] != "#":
            j += 1

        l_word = int(str[i:j])
        strs.append(str[j + 1:j + 1 + l_word])
        i = j + 1 + l_word

    return strs