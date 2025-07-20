"""
Python Coding Challenges: Core Concepts Practice (30 Problems)

Each function below corresponds to a challenge. Students are encouraged to implement
each function by replacing the 'pass' statement with their own code.

Author: OpenAI ChatGPT
"""

# 1. Sum of Digits
def sum_of_digits(n):
    """Return the sum of digits of an integer. E.g., 123 => 6"""
    pass

# 2. Swap Variables
def swap(a, b):
    """Return swapped values. E.g., swap(3, 5) => (5, 3)"""
    pass

# 3. Type Checker
def check_types(lst):
    """Return a list of types of each element in lst. E.g., [1, "hi", 3.0] => [<class 'int'>, <class 'str'>, <class 'float'>]"""
    pass

# 4. String Reversal
def reverse_string(s):
    """Return the reverse of string s. E.g., 'hello' => 'olleh'"""
    pass

# 5. BMI Calculator
def bmi(weight, height):
    """Return BMI and category: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+)."""
    pass

# 6. FizzBuzz
def fizz_buzz():
    """Print numbers from 1 to 100. For multiples of 3 print 'Fizz', for 5 print 'Buzz', for both print 'FizzBuzz'."""
    pass

# 7. Palindrome Check
def is_palindrome(s):
    """Return True if s is a palindrome (reads the same backward). E.g., 'racecar' => True"""
    pass

# 8. Prime Numbers
def primes_less_than(n):
    """Return a list of all prime numbers less than n."""
    pass

# 9. Factorial (Iterative)
def factorial(n):
    """Return the factorial of n using a loop. E.g., 5! => 120"""
    pass

# 10. Number Guessing Game (console-based)
def number_guessing_game():
    """Interactive game: User tries to guess a number between 1 and 100."""
    pass

# 11. Unique Elements
def unique_elements(lst):
    """Return a list of elements that appear only once in lst. E.g., [1,2,2,3] => [1,3]"""
    pass

# 12. Frequency Counter
def char_frequency(s):
    """Return a dictionary of frequency of each character in string s."""
    pass

# 13. List Flattening
def flatten_once(nested_list):
    """Flatten one level of nested list. E.g., [[1,2],[3]] => [1,2,3]"""
    pass

# 14. Top 3 Frequent Words
def top_3_words(text):
    """Return a list of top 3 most frequent words in the given text."""
    pass

# 15. Tuple Sorting
def sort_tuples_by_second(tuples):
    """Sort a list of tuples by the second value. E.g., [(1,3), (4,1)] => [(4,1), (1,3)]"""
    pass

# 16. Leap Year
def is_leap_year(year):
    """Return True if year is a leap year (divisible by 4, not 100 unless also 400)."""
    pass

# 17. Custom Min/Max
def custom_min(lst):
    """Return the minimum value in lst without using min()."""
    pass

def custom_max(lst):
    """Return the maximum value in lst without using max()."""
    pass

# 18. Nested Function
def outer_square(x):
    """Return square of x using a nested function."""
    pass

# 19. Logging with Default Arguments
def log(message, level="INFO"):
    """Log a message with a given level. E.g., log("test") => "[INFO] test""""
    pass

# 20. Args and Kwargs
def print_all_args(*args, **kwargs):
    """Print all positional and keyword arguments."""
    pass

# 21. File Word Counter
def count_words_in_file(filename):
    """Return number of words in a file given by filename."""
    pass

# 22. Copy File
def copy_file(src, dest):
    """Copy content from src file to dest file."""
    pass

# 23. CSV to Dict
def csv_to_dict(filename):
    """Convert a CSV file to a list of dictionaries (header as keys)."""
    pass

# 24. Safe Division
def safe_divide(a, b):
    """Return a / b. If b is 0, return 'Undefined'."""
    pass

# 25. Input Validation
def input_integer():
    """Prompt user for integer input, retry on invalid input."""
    pass

# 26. Multiplication Table
def multiplication_table():
    """Print a 10x10 multiplication table."""
    pass

# 27. Floyd's Triangle
def floyds_triangle(n):
    """Print Floyd's triangle up to n rows using consecutive integers."""
    pass

# 28. Custom Module Import
# Project-based. Create 'mymodule.py' with function and import it into another file.

# 29. Math Practice
def math_operations(x, y):
    """Return a dictionary with sqrt(x), x**y, and log(x) using math module."""
    pass

# 30. Random Password Generator
def generate_password(length):
    """Generate and return a random alphanumeric password of given length."""
    pass

# Main function to run sample test cases
def main():
    print("Sample Tests:")
    print("1. sum_of_digits(123):", sum_of_digits(123))  # Expected: 6
    print("2. swap(5, 10):", swap(5, 10))  # Expected: (10, 5)
    print("3. check_types([1, 'hello', 3.5]):", check_types([1, 'hello', 3.5]))
    print("4. reverse_string('hello'):", reverse_string("hello"))  # Expected: 'olleh'
    print("5. bmi(70, 1.75):", bmi(70, 1.75))  # Expected: (22.86, 'Normal')
    print("6. is_palindrome('madam'):", is_palindrome('madam'))  # Expected: True
    print("7. primes_less_than(10):", primes_less_than(10))  # Expected: [2, 3, 5, 7]
    print("8. factorial(5):", factorial(5))  # Expected: 120
    print("9. unique_elements([1, 2, 2, 3, 4, 4, 5]):", unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Expected: [1, 3, 5]
    print("10. char_frequency('hello'):", char_frequency("hello"))  # Expected: {'h':1, 'e':1, 'l':2, 'o':1}
    print("11. flatten_once([[1, 2], [3], [4, 5]]):", flatten_once([[1, 2], [3], [4, 5]]))  # Expected: [1, 2, 3, 4, 5]
    print("12. top_3_words('apple banana apple orange banana apple'):", top_3_words('apple banana apple orange banana apple'))  # Expected: ['apple', 'banana', 'orange']
    print("13. sort_tuples_by_second([(1, 3), (4, 1), (2, 2)]):", sort_tuples_by_second([(1, 3), (4, 1), (2, 2)]))  # Expected: [(4, 1), (2, 2), (1, 3)]
    print("14. is_leap_year(2020):", is_leap_year(2020))  # Expected: True
    print("15. custom_min([5, 2, 9]):", custom_min([5, 2, 9]))  # Expected: 2
    print("16. custom_max([5, 2, 9]):", custom_max([5, 2, 9]))  # Expected: 9
    print("17. outer_square(4):", outer_square(4))  # Expected: 16
    print("18. log('Test message'):", log('Test message'))  # Expected: [INFO] Test message
    print("19. safe_divide(10, 0):", safe_divide(10, 0))  # Expected: 'Undefined'
    print("20. math_operations(9, 2):", math_operations(9, 2))  # Expected: {'sqrt': 3.0, 'power': 81, 'log': 2.197...}
    print("21. generate_password(10):", generate_password(10))  # Expected: Random 10-char password

if __name__ == "__main__":
    main()
