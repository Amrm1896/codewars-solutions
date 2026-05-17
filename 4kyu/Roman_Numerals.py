class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        dict_roman = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        roman_number = ""
        for key in dict_roman.keys():
            while val >= key:
                val -= key
                roman_number += dict_roman[key]
        return roman_number
    @staticmethod
    def from_roman(roman_num : str) -> int:
        dict_roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=[]
        s=roman_num[::-1]
        for index,digit in enumerate (s) :      
            if index>0 and dict_roman[digit] < dict_roman[s[index-1]]:
                result.append(-dict_roman[digit])
            else:
                result.append(dict_roman[digit])
        return sum(result)
