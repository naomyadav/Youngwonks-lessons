from math import sqrt, log
import math as mt

"""
Python Coding Challenges: Core Concepts Practice (30 Problems)

Each function below corresponds to a challenge. Students are encouraged to implement
each function by replacing the 'pass' statement with their own code.
"""

# 1. Sum of Digits
def sum_of_digits(n):
    """Return the sum of digits of an integer. E.g., 123 => 6"""
    total = 0
    str_n = str(n)
    ln = list(str_n)
    for i in range(len(str_n)):
        total += int(ln[i])
    return total

# 2. Swap Variables
def swap(a, b):
    """Return swapped values. E.g., swap(3, 5) => (5, 3)"""
    c = a
    d = b
    return (d, c)

# 3. Type Checker
def check_types(lst):
    """Return a list of types of each element in lst. E.g., [1, "hi", 3.0] => [<class 'int'>, <class 'str'>, <class 'float'>]"""
    lst_type = [type(lst[i]) for i in range(len(lst))]
    return lst_type

# 4. String Reversal
def reverse_string(s):
    """Return the reverse of string s. E.g., 'hello' => 'olleh'"""
    rev = s[::-1]
    return rev

# 5. BMI Calculator
def bmi(weight, height):
    """Return BMI and category: 
    Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
    bmi_value = weight / (height ** 2) """
    bmi_val = weight / (height ** 2)
    if bmi_val < 18.5:
        bmi_cat = "Underweight"
    elif bmi_val < 25:
        bmi_cat = "Normal"
    elif bmi_val < 30:
        bmi_cat = "Overweight"
    else:
        bmi_cat = "Obese"
    return (bmi_val, bmi_cat)

# 6. FizzBuzz
def fizz_buzz():
    """Print numbers from 1 to 100. For multiples of 3 print 'Fizz', for 5 print 'Buzz', for both print 'FizzBuzz'."""
    count_fizz = 0
    count_buzz = 0
    count_fizzbuzz = 0
    for i in range(1, 101):
        if i % 15 == 0:
            count_fizzbuzz += 1
        elif i % 3 == 0:
            count_fizz += 1
        elif i % 5 == 0:
            count_buzz += 1
    return (count_fizz, count_buzz, count_fizzbuzz)

# 7. Palindrome Check
def is_palindrome(s):
    """Return True if s is a palindrome (reads the same backward). E.g., 'racecar' => True"""
    return s == s[::-1]

# 8. Prime Numbers
def primes_less_than(n):
    """Return a list of all prime numbers less than n."""
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# 9. Factorial (Iterative)
def factorial(n):
    """Return the factorial of n. E.g., 5! => 120
    factorial(n) = n*(n-1)*....*2*3*1
    if n<1 return 1"""
    return mt.factorial(n)

# 10. Student Score Aggregator
def average_scores(records):
    """
    Given a list of tuples representing student names and their test scores,
    return a dictionary mapping each student to their average score.

    Parameters:
    - records: List[Tuple[str, int]]
      Example: [('Alice', 80), ('Bob', 70), ('Alice', 90)]

    Returns:
    - Dict[str, float]
      Example: {'Alice': 85.0, 'Bob': 70.0}

    Rules:
    - Use a loop to accumulate scores.
    - Use a dictionary to track total and count per student.
    - Return a new dictionary with average scores (rounded to 2 decimal places).
    """
    totals = {}
    counts = {}
    for name, score in records:
        totals[name] = totals.get(name, 0) + score
        counts[name] = counts.get(name, 0) + 1
    ret_dict = {k: round(totals[k] / counts[k], 2) for k in totals}
    return ret_dict

# 11. Unique Elements
def unique_elements(lst):
    """Return a list of elements that appear only once in lst. E.g., [1,2,2,3] => [1,3]"""
    from collections import Counter
    c = Counter(lst)
    return [x for x in c if c[x] == 1]

# 12. Frequency Counter
def char_frequency(s):
    """Return a dictionary of frequency of each character in string s."""
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

# 13. List Flattening
def flatten_once(nested_list):
    """Flatten one level of nested list. E.g., [[1,2],[3]] => [1,2,3]"""
    lst_flat = []
    for sublist in nested_list:
        lst_flat += sublist
    return lst_flat

# 14. Top 3 Frequent Words
def top_3_words(text):
    """Return a list of top 3 most frequent words in the given text."""
    if not text:
        return []
    from collections import Counter
    words = text.split()
    c = Counter(words)
    return [w for w, _ in c.most_common(3)]

# 15. Tuple Sorting
def sort_tuples_by_second(tuples):
    """Sort a list of tuples by the second value. E.g., [(1,3), (4,1)] => [(4,1), (1,3)]"""
    return sorted(tuples, key=lambda x: x[1])

# 16. Leap Year
def is_leap_year(year):
    """Return True if year is a leap year (divisible by 4 and only divisible by 100 if divisble by 400)."""
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

# 17. Custom Min/Max
def custom_min(lst):
    """Return the minimum value in lst without using min()."""
    if not lst:
        return None
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

def custom_max(lst):
    """Return the maximum value in lst without using max()."""
    if not lst:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

# 18. Mini calculator
def mini_calculator(a, b, operation):
    """
    Perform a basic operation on two numbers using nested functions.

    Valid operations:
    - 'add'      => a + b
    - 'subtract' => a - b
    - 'multiply' => a * b

    Parameters:
    - a, b: numbers (int or float)
    - operation: string specifying the operation

    Returns:
    - Result of the operation
    - return -99999999999 if invalid operation
    """
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    elif operation == 'multiply':
        return multiply(a, b)
    else:
        return -99999999999

# 19. Logging with Default Arguments
def log(message, level="INFO"):
    """Log a message with a given level. E.g., log("test") => "[INFO] test"""
    return f"[{level}] {message}"

# 20. Filter Even Numbers with List Comprehension
def filter_even_numbers(lst):
    """
    Given a list of integers, return a new list containing only the even numbers.

    Use list comprehension.

    Example:
    filter_even_numbers([1, 2, 3, 4, 5]) => [2, 4]
    """
    return [x for x in lst if x % 2 == 0]

# 21. Square Matrix Transpose (2D List)
def transpose_matrix(matrix):
    """
    Given a 2D list (matrix), return its transpose.

    Example:
    transpose_matrix([[1, 2], [3, 4]]) => [[1, 3], [2, 4]]
    """
    if not matrix:
        return []
    return [list(row) for row in zip(*matrix)]

# 22. Dictionary Inverter
def invert_dictionary(d):
    """
    Invert a dictionary so that keys become values and values become keys.

    Assumes all values are unique.

    Example:
    invert_dictionary({'a': 1, 'b': 2}) => {1: 'a', 2: 'b'}
    """
    return {v: k for k, v in d.items()}

# 23. Count Word Lengths with Dictionary Comprehension
def word_length_dict(words):
    """
    Given a list of words, return a dictionary where keys are words and values are their lengths.

    Use dictionary comprehension.

    Example:
    word_length_dict(['apple', 'hi']) => {'apple': 5, 'hi': 2}
    """
    return {w: len(w) for w in words}

# 24. Safe Division
def safe_divide(a, b):
    """
    For two numbers and divide them.
    Handle ValueError (non-numeric input) and ZeroDivisionError.

    Returns:
    - Result of division or error message"""
    try:
        return a / b
    except Exception:
        return 'Error'

# 25. Safe Dictionary Lookup
def safe_lookup(d, key):
    """
    Attempt to retrieve the value for the given key from dictionary d.

    Uses try-except to handle KeyError.

    Parameters:
    - d: dictionary
    - key: key to look up

    Returns:
    - The value associated with the key if it exists
    - The string "Key not found" if the key does not exist

    Example:
    >>> safe_lookup({'a': 1, 'b': 2}, 'a')
    1
    >>> safe_lookup({'a': 1, 'b': 2}, 'c')
    'Key not found'
    """
    try:
        return d[key]
    except KeyError:
        return 'Key not found'

# 26. Multiplication Table
def multiplication_table():
    """Print a 10x10 multiplication table."""
    # Return sum of diagonal elements
    sum_diag_elem = sum(i * i for i in range(1, 11))
    return sum_diag_elem

# 27. Floyd's Triangle
def floyds_triangle(n):
    """
    Print Floyd's Triangle up to n rows using consecutive integers starting from 1.

    Example for n = 5:
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15

    Parameters:
    - n: int, number of rows to print
    """
    # Return sum of numbers in last row
    start = 1
    last_row_sum = 0
    for i in range(1, n + 1):
        row_numbers = []
        for j in range(i):
            row_numbers.append(start)
            start += 1
        if i == n:
            last_row_sum = sum(row_numbers)
    return last_row_sum

# 28. Math Practice
def math_operations(x, y):
    """Return a dictionary with sqrt(x), x**y, and log(x) using math module."""
    return {"sqrt": sqrt(x), "power": x ** y, "log": log(x)}

# 29. Random Password Generator
def generate_password(length):
    """
    Generate and return a random alphanumeric password of given length.

    Rules:
    - Must include at least one lowercase letter
    - Must include at least one uppercase letter
    - Must include at least one digit
    - Remaining characters can be letters or digits
    - Length must be at least 6 characters

    Returns:
    - A string representing the password
    """
    import random
    import string
    if length < 6:
        return "Password length must be at least 6"
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    rest_len = length - 3
    rest = [random.choice(string.ascii_letters + string.digits) for _ in range(rest_len)]
    pwd_list = [lower, upper, digit] + rest
    random.shuffle(pwd_list)
    return ''.join(pwd_list)

# 30. Password Validation
def is_valid_password(password):
    """
    Check if the given password meets the required rules.

    Rules:
    - At least 8 characters
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit

    Returns:
    - True if valid, False otherwise
    """
    import re
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    return True

# Main function to run sample test cases
def main():
    print("Sample Tests with 3 Cases Each:")

    print("1.", sum_of_digits(123) == 6 and sum_of_digits(0) == 0 and sum_of_digits(999) == 27)
    print("2.", swap(1, 2) == (2, 1) and swap('a', 'b') == ('b', 'a') and swap(True, False) == (False, True))
    print("3.", check_types([1, 'x', 2.5]) == [int, str, float] and check_types([]) == [] and check_types([None]) == [type(None)])
    print("4.", reverse_string('cat') == 'tac' and reverse_string('') == '' and reverse_string('a') == 'a')
    print("5.", bmi(45, 1.6)[1] == 'Underweight' and bmi(65, 1.7)[1] == 'Normal' and bmi(90, 1.6)[1] == 'Obese')
    print("6.", fizz_buzz() == (27, 14, 6))
    print("7.", is_palindrome('level') and not is_palindrome('hello') and is_palindrome('Aibohphobia'.lower()))
    print("8.", primes_less_than(2) == [] and primes_less_than(10) == [2, 3, 5, 7] and primes_less_than(20)[-1] == 19)
    print("9.", factorial(0) == 1 and factorial(1) == 1 and factorial(4) == 24)
    print("10.", average_scores([('Alice', 80), ('Bob', 70), ('Alice', 90)]) == {'Alice': 85.0, 'Bob': 70.0}
            and average_scores([]) == {} 
            and average_scores([('Charlie', 100), ('Charlie', 50), ('Charlie', 75)]) == {'Charlie': 75.0})
    print("11.", unique_elements([1,1,2,3,3]) == [2] and unique_elements([]) == [] and unique_elements([4,5,4,6]) == [5,6])
    print("12.", char_frequency('aab') == {'a':2,'b':1} and char_frequency('') == {} and char_frequency('abcabc') == {'a':2,'b':2,'c':2})
    print("13.", flatten_once([[1,2],[3]]) == [1,2,3] and flatten_once([]) == [] and flatten_once([[1],[2],[3]]) == [1,2,3])
    print("14.", top_3_words('one two one three two one') == ['one', 'two', 'three'] and top_3_words('a b c') == ['a','b','c'] and top_3_words('') == [])
    print("15.", sort_tuples_by_second([(1,2),(3,1)]) == [(3,1),(1,2)] and sort_tuples_by_second([]) == [] and sort_tuples_by_second([(5,5)]) == [(5,5)])
    print("16.", is_leap_year(2000) == True and is_leap_year(1900) == False and is_leap_year(2024) == True)
    print("17.", custom_min([3,2,1]) == 1 and custom_min([100]) == 100 and custom_min([-1,0]) == -1)
    print("17.", custom_max([3,2,1]) == 3 and custom_max([100]) == 100 and custom_max([-1,0]) == 0)
    print("18.", mini_calculator(2,3,'add') == 5 and mini_calculator(5,2,'subtract') == 3 and mini_calculator(2,3,'multiply') == 6)
    print("19.", log('hi') == '[INFO] hi' and log('warn', level='WARNING') == '[WARNING] warn' and log('err', level='ERROR') == '[ERROR] err')
    print("20.", filter_even_numbers([1,2,3]) == [2] and filter_even_numbers([]) == [] and filter_even_numbers([2,4,6]) == [2,4,6])
    print("21.", transpose_matrix([[1]]) == [[1]] and transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]] and transpose_matrix([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]])
    print("22.", invert_dictionary({'a':1}) == {1:'a'} and invert_dictionary({'x':9,'y':8}) == {9:'x',8:'y'} and invert_dictionary({}) == {})
    print("23.", word_length_dict(['hi']) == {'hi':2} and word_length_dict(['a','ab']) == {'a':1,'ab':2} and word_length_dict([]) == {})
    print("24.", safe_divide(8,4) == 2.0 and safe_divide(5,0) == 'Error' and isinstance(safe_divide('a','b'), str))
    print("25.", safe_lookup({'x':1},'x') == 1 and safe_lookup({'x':1},'y') == 'Key not found' and safe_lookup({},'z') == 'Key not found')
    print("26.", multiplication_table() == 385)  # diagonal sum 1+4+...+100
    print("27.", floyds_triangle(1) == 1 and floyds_triangle(3) == 12 and floyds_triangle(5) == 65)
    print()
    print("28.", math_operations(4,2)['power'] == 16 and math_operations(9,2)['sqrt'] == 3 and 'log' in math_operations(10,1))
    print("29.", len(generate_password(10)) == 10 and is_valid_password(generate_password(10)) == True and generate_password(5) == "Password length must be at least 6")
    print("30.", is_valid_password('Abc12345') == True and is_valid_password('abc') == False and is_valid_password('ABC12345') == False)

if __name__ == "__main__":
    main()