ARABIC_TO_ROMAN = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
                   20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C',
                   200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                   2000: 'MM', 3000: 'MMM'}
DECIMAL_POSITIONS = [1, 10, 100, 1000]


def decimal_positions(num):
    position_numbers = []
    while num > 9:
        num, singular_value = divmod(num, 10)
        position_numbers.append(singular_value)

    position_numbers.append(num)
    return position_numbers


def make_tens_hundreds_thousands(list_of_numbers):
    return [value*DECIMAL_POSITIONS[index] for index, value in enumerate(list_of_numbers)]


def convert_number(arabic_number):
    if arabic_number <= 0 or arabic_number >= 4000:
        raise ValueError("Out of range [1, 3999]")

    positions = decimal_positions(arabic_number)
    positions = make_tens_hundreds_thousands(positions)
    decimal_roman_numbers = [ARABIC_TO_ROMAN.get(number, "") for number in positions]

    roman_number = ''.join(decimal_roman_numbers[::-1])
    return roman_number
