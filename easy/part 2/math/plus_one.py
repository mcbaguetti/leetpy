def plus_one(digits):
        carry, i = 1, 0

        digits = digits[::-1]

        while carry:
                if i < len(digits):
                        if digits[i] == 9:
                                digits[i] = 0

                        else:
                                digits[i] += 1
                                carry = 0
                ## 9 -> 10
                else:
                       digits.append(1)
                       carry = 0

                i += 1

        return digits[::-1]