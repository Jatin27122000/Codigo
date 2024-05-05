'''Write a  Python program to create the next bigger number by rearranging the digits of a given number.
Original number: 12
Next bigger number: 21
Original number: 10
Next bigger number: False
Original number: 201
Next bigger number: 210
Original number: 102
Next bigger number: 120
Original number: 445
Next bigger number: 454'''

def next_bigger_number(num):
    digits = list(str(num))
    
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    if i == -1:
        return False 
    
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    next_bigger = int(''.join(digits))
    
    return next_bigger

test_cases = [12, 10, 201, 102, 445]
for num in test_cases:
    next_bigger = next_bigger_number(num)
    print(f"Original number: {num}")
    print("Next bigger number:", next_bigger if next_bigger else False)
