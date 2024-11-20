def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    roman = roman.upper()
    total = 0
    prev_value = 0
    
    numeral_values = [roman_values.get(char, 0) for char in reversed(roman)]
    
    if any(value == 0 for value in numeral_values):
        return "Invalid Roman numeral!"
    
    repeat_counts = {} 

    for value in numeral_values:
        repeat_counts[value] = repeat_counts.get(value, 0) + 1
        if repeat_counts[value] > 3:  
            return "Invalid Roman numeral!"
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total

roman_input = input("Enter a Roman numeral: ")
result = roman_to_integer(roman_input)
print(f"The integer value of '{roman_input.upper()}' is: {result}")
