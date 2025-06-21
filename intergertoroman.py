class IntergerRoman:
    def __init__(self, number):
        self.number = number
    def convert(self):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XM", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ""
        num = self.number
        for i in range(len(val)):
            roman_num += syms[i]
            num -= val[i]
        return roman_num