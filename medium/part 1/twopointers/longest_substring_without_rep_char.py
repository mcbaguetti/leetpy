

def longestSubs(s):
    subSet = set()
    l, res = 0, 0

    for r in range(len(s)):
        while s[r] in subSet:
            subSet.remove(s[l])
            l += 1

        subSet.add(s[r])
        res = max(res, r - l + 1)

    return res
