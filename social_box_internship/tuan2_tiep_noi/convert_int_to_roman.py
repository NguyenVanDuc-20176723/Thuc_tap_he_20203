class ConvertIntToRoman:

    def __init__(self, number):
        self.number = number

    def cvt_int2roman(self):
        str = ""
        num = self.number
        if num < 1 or num > 3999:
            str += "Invalid Roman Number Value!"
        else:
            numerals = {"M": 1000, "CM": 900, "D": 500,
                        "CD": 400, "C": 100, "XC": 90,
                        "L": 50, "XL": 40, "X": 10,
                        "IX": 9, "V": 5, "IV": 4, "I": 1}

            for item in numerals:
                if num >= numerals[item]:
                    str += item * int(num / numerals[item])
                    num %= numerals[item]
        return str


for x in range(0, 100):
    convert = ConvertIntToRoman(x)
    roman = convert.cvt_int2roman()
    print(x, roman)
