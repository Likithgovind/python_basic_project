def roman_to_number(num):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    total = 0
    value = 0

    for i in reversed(num):
        current = roman[i]
        if current < value:
            total -= current
        else:
            total += current
        value = current
    return total
num = input("n=").upper()
print(roman_to_number(num))
