"""342. Power of Four
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true


Example 4:
Input: n = -16
Output: false


Constraints:

    -231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


# the interesting part of this problem is to solve it without recursion or loops
def is_power_of_four(n: int) -> bool:

    if n <= 0:
        return False

    if n == 1:
        return True

    str_bin = str(bin(n))
    sliced = str_bin[2:]
    num_zero = sliced.count('0')

    if int(sliced[0]) == 1 and num_zero % 2 == 0 and (len(sliced) - 1) == num_zero:
        return True

    return False


print(is_power_of_four(-2147483648))


# without count function
def is_pow_of_four(n):
    return 0 < n == (n & 0x55555555) and (n & n - 1 == 0)


"""
first condition: n > 0 
n it musts be greater than 0

third condition: (n & n - 1 == 0)
this checks if n is a power of 2 
f.e. 
    10 & (10-1) == 10 & 01 == 0
    100 & (100-1) == 100 & 011 == 0
    etc.

second condition: n == (n & 0x55555555)
this means to check if "1" is located at the odd position because for power of 4, the additional restriction is that 
in binary form, the only "1" should always located at the odd position.
f.e. 
    4 == 100 (the only 1 is at the odd position) ==> is pow of four
    32 == 100000 (the only 1 is at the even position) ==> is not pow of four

Take the power of 2 and bitwise AND it with the bitmask 0101 0101 = 0x55, 
and then you can see that every other power of 2 is set.

First power of 2 is 1
0000 0001 = 1
0101 0101 = 0x55
0000 0001 = bitwise AND of 1 and 0x55 is 1 and so 1 is a power of 4

Second power of 2 is 2
0000 0010 = 2
0101 0101 = 0x55
0000 0000 = bitwise AND of 2 and 0x55 is 0 and so 2 is NOT a power of 4

Third power of 2 is 4
0000 0100 = 4
0101 0101 = 0x55
0000 0100 = bitwise AND of 4 and 0x55 is 4 and so 4 is a power of 4

Fourth power of 2 is 8
0000 1000 = 8
0101 0101 = 0x55
0000 0000 = bitwise AND of 8 and 0x55 is 0 and so 8 is NOT a power of 4

etc...
etc...

Can you see the pattern of every other power of 2 being a power of 4?
"""