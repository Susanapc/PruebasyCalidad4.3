# pylint: disable=invalid-name
#!/usr/bin/env python3
"""
wordCount.py

A script to count the frequency of distinct words in a given text file.

Usage:
    python wordCount.py fileWithData.txt
"""

import sys
import time

def read_file(file_path):
    """Read the content of the file and return as a string."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return None

def count_words(text):
    """Count the frequency of each distinct word in the text."""
    word_freq = {}
    word = ''
    for char in text:
        if char.isalnum():
            word += char.lower()
        else:
            if word:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
                word = ''
    if word:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def write_results(word_freq, elapsed_time):
    """Write the word frequencies and elapsed time to a file and print to console."""
    try:
        with open('WordCountResults.txt', 'w', encoding='utf-8') as file:
            for word, count in sorted(word_freq.items()):
                line = f"{word}: {count}\n"
                file.write(line)
                print(line, end='')
            time_info = f"\nTime elapsed: {elapsed_time:.4f} seconds\n"
            file.write(time_info)
            print(time_info, end='')
    except IOError as e:
        print(f"Error writing results to file: {e}")

def main():
    """
    This is the main function that invokes the rest of the functions in the module
    """
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    file_path = sys.argv[1]
    start_time = time.time()

    text = read_file(file_path)
    if text is None:
        return

    word_freq = count_words(text)
    elapsed_time = time.time() - start_time

    write_results(word_freq, elapsed_time)

if __name__ == '__main__':
    main()
