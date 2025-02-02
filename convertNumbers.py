"""
This module provides functions to convert numbers from decimal to bunary
and from decimal to hexadecimal.
"""
# pylint: disable=invalid-name
import time
import argparse
def parse_arguments():
    """
    This module is an argument parser.
    """
    parser = argparse.ArgumentParser(description='Convert numbers to binary and hexadecimal.')
    parser.add_argument('filename', type=str, help='Input file containing a list of numbers')
    return parser.parse_args()

def read_numbers_from_file(filename):
    """
    This module is used to read numbers from a file.
    """
    numbers = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Error: Invalid data on line {line_number}: '{line.strip()}'")
    return numbers

def decimal_to_binary(n):
    """
    This module converts from decimal to binary.
    """
    if n == 0:
        return '0'
    binary = ''
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    if is_negative:
        binary = '-' + binary
    return binary

def decimal_to_hexadecimal(n):
    """
    This module converts from decimal to hexadecimal.
    """
    if n == 0:
        return '0'
    hex_chars = '0123456789ABCDEF'
    hexadecimal = ''
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    if is_negative:
        hexadecimal = '-' + hexadecimal
    return hexadecimal

def write_results_to_file_and_screen(numbers, binary_reprs, hex_reprs, execution_time):
    """
    This module writes the results to a file.
    """
    with open('ConvertionResults.txt', 'w', encoding='utf-8') as file:
        for number, binary, hexadecimal in zip(numbers, binary_reprs, hex_reprs):
            result = f"Number: {number}, Binary: {binary}, Hexadecimal: {hexadecimal}"
            print(result)
            file.write(result + '\n')
        time_info = f"Time elapsed: {execution_time:.4f} seconds"
        print(time_info)
        file.write(time_info + '\n')

def main():
    """
    This the main function that invokes the rest of the functions.
    """
    args = parse_arguments()
    start_time = time.time()
    numbers = read_numbers_from_file(args.filename)
    binary_reprs = [decimal_to_binary(n) for n in numbers]
    hex_reprs = [decimal_to_hexadecimal(n) for n in numbers]
    execution_time = time.time() - start_time
    write_results_to_file_and_screen(numbers, binary_reprs, hex_reprs, execution_time)

if __name__ == '__main__':
    main()
