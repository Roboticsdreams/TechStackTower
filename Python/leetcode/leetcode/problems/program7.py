class ReverseInteger:
    """"
    Reverse Integer [Medium]

    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:
    Input: x = 123
    Output: 321

    Example 2:
    Input: x = -123
    Output: -321

    Example 3:
    Input: x = 120
    Output: 21

    Example 4:
    Input: x = 0
    Output: 0

    Constraints:
    -231 <= x <= 231 - 1
    """
    def reverse(self, x: int) -> int:
        result = 0
        max_int = 2 ** 31
        min_int = -2 ** 31
        if x > 0:
            neg = 0
        else:
            neg = 1
            x = x * -1

        while x != 0:
            mod = x % 10
            result = int(result * 10 + mod)
            x = (x - mod) / 10
            if result > max_int or result < min_int:
                return 0

        if neg:
            return result * -1
        else:
            return result

def reverseinteger_main():
    p7 = ReverseInteger()
    return p7.reverse(-321)