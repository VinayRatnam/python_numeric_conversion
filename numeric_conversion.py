#Vinay Ratnam
#10/02/23

import math #can now use functions from math module

def decoding_menu(): #function for menu
    print('Decoding Menu')
    print('-------------')
    print('1. Decode hexadecimal')
    print('2. Decode binary')
    print('3. Convert binary to hexadecimal')
    print('4. Quit\n')

def hex_char_decode(digit):
    """Decodes a single hexadecimal digit and returns its value"""
    single_hex_decoded_value = ''
    if digit.upper() == 'A':
        single_hex_decoded_value = 10
    elif digit.upper() == 'B':
        single_hex_decoded_value = 11
    elif digit.upper() == 'C':
        single_hex_decoded_value = 12
    elif digit.upper() == 'D':
        single_hex_decoded_value = 13
    elif digit.upper() == 'E':
        single_hex_decoded_value = 14
    elif digit.upper() == 'F':
        single_hex_decoded_value = 15
    elif 0 <= int(digit) <= 9:
        single_hex_decoded_value = int(digit)
    return single_hex_decoded_value

def hex_string_decode(hex):
    """Decodes an entire hexadecimal string and returns its value"""
    if hex[0:2] == '0x':
        hex = hex[2:len(hex)]
    sum = 0
    for i in range(0, len(hex)):
        num = hex_char_decode(hex[i]) * math.pow(16, len(hex) - 1 - i)
        sum += num
    return sum

def binary_string_decode(binary):
    """Decodes a binary string and returns its value"""
    if binary[0:2] == '0b':
        binary = binary[2:len(binary)]
    sum = 0
    for i in range(0, len(binary)):
        num = int(binary[i]) * math.pow(2, len(binary) - 1 - i)
        sum += num
    return sum

def base_10_to_hex(base_10):
    """Codes a value into a hexadecimal character"""
    hex_value = ''
    if 0 <= base_10 <= 9:
        hex_value = str(int(base_10))
    elif base_10 == 10:
        hex_value = 'A'
    elif base_10 == 11:
        hex_value = 'B'
    elif base_10 == 12:
        hex_value = 'C'
    elif base_10 == 13:
        hex_value = 'D'
    elif base_10 == 14:
        hex_value = 'E'
    elif base_10 == 15:
        hex_value = 'F'
    return hex_value

def binary_to_hex(binary):
    """Codes a binary string into a hexadecimal string"""
    hex_conversion = ''
    base_10_conversion = 0
    if binary[0:2] == '0b':
        binary = binary[2:len(binary)]
    for i in range(0, int(len(binary) / 4)):
        base_10_conversion = binary_string_decode(binary[4 * i:4 * i + 4])
        hex_char = base_10_to_hex(base_10_conversion)
        hex_conversion += hex_char
    return hex_conversion

def main():
    converted_num = 0
    condition = True
    while condition == True:
        decoding_menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 4:
            print('Goodbye!')
            break
        if menu_option == 1:
            converted_num = hex_string_decode(input('Please enter the numeric string to convert: '))
            print(f'Result: {converted_num:.0f}')
        elif menu_option == 2:
            converted_num = binary_string_decode(input('Please enter the numeric string to convert: '))
            print(f'Result: {converted_num:.0f}')
        elif menu_option == 3:
            converted_num = binary_to_hex(input('Please enter the numeric string to convert: '))
            print(f'Result: {converted_num}')
        print()

if __name__=="__main__":
    main()