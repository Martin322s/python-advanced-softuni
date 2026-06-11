class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        else:
            return "value is not a float"
    
    @classmethod
    def from_roman(cls, value):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if isinstance(value, str) and all(char in roman_numerals for char in value):
            total = 0
            prev_value = 0
            for char in reversed(value):
                current_value = roman_numerals[char]
                if current_value < prev_value:
                    total -= current_value
                else:
                    total += current_value
                prev_value = current_value
            return cls(total)
        else:
            return "wrong type"
    
    @classmethod
    def from_string(cls, value):
        if isinstance(value, str) and value.isdigit():
            return cls(int(value))
        else:
            return "wrong type"