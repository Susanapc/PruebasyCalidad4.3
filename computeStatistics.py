#!/usr/bin/env python3

import sys
import time

def read_numbers_from_file(filename):
    """Read numbers from a file, ignoring invalid lines."""
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Invalid data encountered and skipped: {line.strip()}")
    return numbers

def calculate_mean(numbers):
    """Calculate the mean of a list of numbers."""
    total = sum(numbers)
    count = len(numbers)
    return total / count

def calculate_median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    middle = count // 2
    if count % 2 == 0:
        return (sorted_numbers[middle - 1] + sorted_numbers[middle]) / 2
    else:
        return sorted_numbers[middle]

def calculate_mode(numbers):
    """Calculate the mode of a list of numbers."""
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    max_count = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_count]
    if len(modes) == 1:
        return modes[0]
    else:
        return modes  # In case of multimodal data

def calculate_variance(numbers, mean):
    """Calculate the variance of a list of numbers."""
    sum_squared_diff = sum((x - mean) ** 2 for x in numbers)
    return sum_squared_diff / len(numbers)

def calculate_standard_deviation(variance):
    """Calculate the standard deviation from variance."""
    return variance ** 0.5

def write_results_to_file(filename, results):
    """Write the statistical results to a file."""
    with open(filename, 'w') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = 'StatisticsResults.txt'

    start_time = time.time()

    numbers = read_numbers_from_file(input_filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    standard_deviation = calculate_standard_deviation(variance)

    results = {
        'Mean': mean,
        'Median': median,
        'Mode': mode,
        'Variance': variance,
        'Standard Deviation': standard_deviation
    }

    for key, value in results.items():
        print(f"{key}: {value}")

    write_results_to_file(output_filename, results)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time elapsed: {elapsed_time:.4f} seconds")

    with open(output_filename, 'a') as file:
        file.write(f"Time elapsed: {elapsed_time:.4f} seconds\n")

if __name__ == "__main__":
    main()  