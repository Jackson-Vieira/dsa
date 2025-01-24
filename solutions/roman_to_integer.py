class Solution(object):

    roman_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        result = 0
        previous_value = 0
        for roman_letter in s[::-1]:
            current_value = self.roman_dict[roman_letter]
            if(current_value < previous_value):
                current_value *= -1
            result += current_value
            previous_value = current_value

        return result

class Test:
    def test_given_I_should_return_1(self):
        case = "I"
        expected = 1

        assert Solution().romanToInt(case) == expected
    def test_given_III_should_return_3(self):
        case = "III"
        expected = 3

        assert Solution().romanToInt(case) == expected

    def test_given_X_should_return_10(self):
        case = "X"
        expected = 10

        assert Solution().romanToInt(case) == expected

    def test_given_XV_should_return_10(self):
        case = "XV"
        expected = 15

        assert Solution().romanToInt(case) == expected

    def test_should_discount_if_current_letter_is_smaller_than_previous(self):
        case = "XIV"
        expected = 14

        assert Solution().romanToInt(case) == expected
