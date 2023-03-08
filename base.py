#in development
def binary_calculator(num1, num2, operator):
    if operator == '+':
        return bin(int(num1, 2) + int(num2, 2))[2:]
    elif operator == '-':
        return bin(int(num1, 2) - int(num2, 2))[2:]
    elif operator == '*':
        return bin(int(num1, 2) * int(num2, 2))[2:]
    elif operator == '/':
        return bin(int(num1, 2) // int(num2, 2))[2:]
    else:
        return None

def text_to_binary(text):
    binary_string = ""
    for char in text:
        binary_string += bin(ord(char))[2:].zfill(8)
    return binary_string

def binary_to_base(binary_string, base):
    decimal_num = int(binary_string, 2)
    if base == 2:
        return binary_string
    elif base == 8:
        return oct(decimal_num)[2:]
    elif base == 10:
        return str(decimal_num)
    elif base == 16:
        return hex(decimal_num)[2:]

# Example usage:
print(binary_calculator('1010', '1100', '+')) # Output: '10110'
print(text_to_binary('hello world')) # Output: '0110100001100101011011000110110001101111001000000111011101101111011100100110110001100100'
print(binary_to_base('10101010', 10)) # Output: '170'
print(binary_to_base('10101010', 16)) # Output: 'aa'
