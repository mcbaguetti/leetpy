"""371. Sum of Two Integers
Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Example 3:
Input: a = -1, b = 3
Output: 2
 """


# this is a lot tricky, for solving this without +, - and any built-in library function you must know:
#       - bit manipulation like shiftLeft and shiftRight,
#       - bitwise logic operators like &, ^, |, ~,
#       - and (only if you write this program in python like me) masks because python allows unlimited length of
#          integers unlike java which limits integers' size to 32-bit

def get_sum(self, a: int, b: int) -> int:
    mask = 0xffffffff

    while b:
        tot_sum = (a ^ b) & mask
        carry = ((a & b) << 1) & mask
        a = tot_sum
        b = carry

    #  If a is negative in 32 bits sense and it has been & masked already.
    if (a >> 31) & 1 and ~(a >> 32):
        return ~(a ^ mask)

    return a
