values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


class Solution:
    def romanToInt(self, string: str) -> int:
        sum = 0

        while string:
            double_number = values.get(string[:2])
            if double_number:
                sum += double_number
                string = string[2:]
            else:
                sum += values[string[0]]
                string = string[1:]

        return sum
