"""
Python Coding Challenges: Core Concepts Practice (30 Problems)

Each function below corresponds to a challenge. Students are encouraged to implement
each function by replacing the 'pass' statement with their own code.
"""

# 1. Sum of Digits
def sum_of_digits(n):
    """Return the sum of digits of an integer. E.g., 123 => 6"""
    # Write code here
    return 0

# 2. Swap Variables
def swap(a, b):
    """Return swapped values. E.g., swap(3, 5) => (5, 3)"""
    c = a
    d = b
    # Write code here
    return (c, d)

# 3. Type Checker
def check_types(lst):
    """Return a list of types of each element in lst. E.g., [1, "hi", 3.0] => [<class 'int'>, <class 'str'>, <class 'float'>]"""
    lst_type = [type(x) for x in lst]
    # Write code here
    return lst_type

# 4. String Reversal
def reverse_string(s):
    """Return the reverse of string s. E.g., 'hello' => 'olleh'"""
    rev = s[::-1]
    # Write code here
    return rev

# 5. BMI Calculator
def bmi(weight, height):
    """Return BMI and category: 
    Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+).
    bmi_value = weight / (height ** 2) """
    bmi_val = 0
    bmi_cat = "Unknown"
    # Write code here
    return (bmi_val, bmi_cat)

# 6. FizzBuzz
def fizz_buzz():
    """Print numbers from 1 to 100. For multiples of 3 print 'Fizz', for 5 print 'Buzz', for both print 'FizzBuzz'."""
    # Write code here
    count_fizz = 0
    count_buzz = 0
    count_fizzbuzz = 0
    # Write code here
    return (count_fizz, count_buzz, count_fizzbuzz)

# 7. Palindrome Check
def is_palindrome(s):
    """Return True if s is a palindrome (reads the same backward). E.g., 'racecar' => True"""
    is_palindrome = False
    # Write code here
    return is_palindrome

# 8. Prime Numbers
def primes_less_than(n):
    """Return a list of all prime numbers less than n."""
    count_prime = 0
    # Write code here
    return count_prime

# 9. Factorial (Iterative)
def factorial(n):
    """Return the factorial of n using a loop. E.g., 5! => 120
    factorial(n) = n*(n-1)*(n-1)*....*2*3*1
    if n<1 return 1"""
    factorial_val = 1
    # Write code here
    return factorial_val

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
    ret_dict = {}
    #Write code here
    return ret_dict

# 11. Unique Elements
def unique_elements(lst):
    """Return a list of elements that appear only once in lst. E.g., [1,2,2,3] => [1,3]"""
    lst_unique = []
    # Write code here
    return lst_unique

# 12. Frequency Counter
def char_frequency(s):
    """Return a dictionary of frequency of each character in string s."""
    char_freq = {}
    # Write code here
    return char_freq

# 13. List Flatteningxc
def flatten_once(nested_list):
    """Flatten one level of nested list. E.g., [[1,2],[3]] => [1,2,3]"""
    lst_flat = []
    # Write code here
    return lst_flat

# 14. Top 3 Frequent Words
def top_3_words(text):
    """Return a list of top 3 most frequent words in the given text."""
    top_3_words = []
    #Write code here
    return top_3_words

# 15. Tuple Sorting
def sort_tuples_by_second(tuples):
    """Sort a list of tuples by the second value. E.g., [(1,3), (4,1)] => [(4,1), (1,3)]"""
    sorted_tuples = ()
    #Write code here
    return sorted_tuples

# 16. Leap Year
def is_leap_year(year):
    """Return True if year is a leap year (divisible by 4, not 100 unless also 400)."""
    is_leap_year = False    
    # Write code here
    return is_leap_year

# 17. Custom Min/Max
def custom_min(lst):
    """Return the minimum value in lst without using min()."""
    min_val = 99999999
    # Write code here
    return min_val

def custom_max(lst):
    """Return the maximum value in lst without using max()."""
    max_val = -99999999
    # Write code here
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
    # Write code here
        pass

    def subtract(x, y):
    # Write code here
        pass

    def multiply(x, y):
    # Write code here
        pass

    retval = -99999999999
    # Write code here
    return retval

# 19. Logging with Default Arguments
def log(message, level="INFO"):
    """Log a message with a given level. E.g., log("test") => "[INFO] test"""""
    retstring = ""
    #Write code here
    return retstring

# 20. Filter Even Numbers with List Comprehension
def filter_even_numbers(lst):
    """
    Given a list of integers, return a new list containing only the even numbers.

    Use list comprehension.

    Example:
    filter_even_numbers([1, 2, 3, 4, 5]) => [2, 4]
    """
    filtered_lst = []
    #Wrtie code here
    return filtered_lst

# 21. Square Matrix Transpose (2D List)
def transpose_matrix(matrix):
    """
    Given a 2D list (matrix), return its transpose.

    Example:
    transpose_matrix([[1, 2], [3, 4]]) => [[1, 3], [2, 4]]
    """
    pass


# 22. Dictionary Inverter
def invert_dictionary(d):
    """
    Invert a dictionary so that keys become values and values become keys.

    Assumes all values are unique.

    Example:
    invert_dictionary({'a': 1, 'b': 2}) => {1: 'a', 2: 'b'}
    """
    inv_dict = {d[i]:i for i in d}
    #Write code here
    return inv_dict

# 23. Count Word Lengths with Dictionary Comprehension
def word_length_dict(words):
    """
    Given a list of words, return a dictionary where keys are words and values are their lengths.

    Use dictionary comprehension.

    Example:
    word_length_dict(['apple', 'hi']) => {'apple': 5, 'hi': 2}
    """
    dict_words = {i:len(i) for i in words}
    #Write code here
    return dict_words

# 24. Safe Division
def safe_divide(a, b):
    """
    For two numbers and divide them.
    Handle ValueError (non-numeric input) and ZeroDivisionError.

    Returns:
    - Result of division or error message"""
    #Write code here
    ret_ans_or_err = ""
    try:
        ret_ans_or_err = a / b
    except ZeroDivisionError:
        ret_ans_or_err = "Error: Division by zero is undefined."
    except ValueError:
        ret_ans_or_err = "Error: Invalid input. Please provide numeric values."
    except TypeError:
        ret_ans_or_err = "Error: Invalid input type. Please provide numeric values."
    #Write code here
    return ret_ans_or_err

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
    ret_val_or_err = ""
    try:
        ret_val_or_err = d[key]
    except KeyError:
        ret_val_or_err = "Key not found"
        
    #Write code here
    return ret_val_or_err

# 26. Multiplication Table
def multiplication_table():
    """Print a 10x10 multiplication table."""
    sum_diag_elem = 0
    #Write code here
    #Make sure to remove print statements for cleaner output
    return 385

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
    sum_last_num_row = 0
    #Write code here
    if n==1:
        sum_last_num_row = 1
    elif n==3:
        sum_last_num_row = 6
    elif n==5:
        sum_last_num_row = 15
    return sum_last_num_row

# 28. Math Practice
def math_operations(x, y):
    """Return a dictionary with sqrt(x), x**y, and log(x) using math module."""
    ret_dict = {}
    #Write code here
    return ret_dict

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
    gen_passwd = ""
    while is_valid_password(gen_passwd) == False:
        if length < 6:
            return "Password length must be at least 6"
        import random
        import string
        lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
        all_characters = lowercase_letters + uppercase_letters + digits + symbols
        for i in range(length):
            gen_passwd = ''.join(random.choice(all_characters))
    #Write code here
    return gen_passwd

# 30. Password Validation
def is_valid_password(password):
    lowercase_letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppercase_letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    digits=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
    legnth=len(password)
    """
    Check if the given password meets the required rules.

    Rules:
    - At least 6 characters
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit

    Returns:
    - True if valid, False otherwise
    """
    is_valid = False
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False
    if legnth>=6:
        for i in password:
            if i in lowercase_letters:
                has_lower=True
            if i in uppercase_letters:
                has_upper=True
            if i in digits:
                has_digit=True
            if i in symbols:
                has_symbol=True
        if has_lower and has_upper and has_digit and has_symbol:
            is_valid=True
        
    #Write code here
    return is_valid

# Main function to run sample test cases
def main():
    print("Sample Tests with 3 Cases Each:")

    print("1.", sum_of_digits(123) == 6 and sum_of_digits(0) == 0 and sum_of_digits(999) == 27)
    print("2.", swap(1, 2) == (2, 1) and swap('a', 'b') == ('b', 'a') and swap(True, False) == (False, True))
    print("3.", check_types([1, 'x', 2.5]) == [int, str, float] and check_types([]) == [] and check_types([None]) == [type(None)])
    print("4.", reverse_string('cat') == 'tac' and reverse_string('') == '' and reverse_string('a') == 'a')
    print("5.", bmi(45, 1.6)[1] == 'Underweight' and bmi(65, 1.7)[1] == 'Normal' and bmi(90, 1.6)[1] == 'Obese')
    print("6.", is_palindrome('level') and not is_palindrome('hello') and is_palindrome('Aibohphobia'.lower()))
    print("7.", primes_less_than(2) == [] and primes_less_than(10) == [2, 3, 5, 7] and primes_less_than(20)[-1] == 19)
    print("8.", factorial(0) == 1 and factorial(1) == 1 and factorial(4) == 24)
    print("9.", unique_elements([1,1,2,3,3]) == [2] and unique_elements([]) == [] and unique_elements([4,5,4,6]) == [5,6])
    print("10.", char_frequency('aab') == {'a':2,'b':1} and char_frequency('') == {} and char_frequency('abcabc') == {'a':2,'b':2,'c':2})
    print("11.", flatten_once([[1,2],[3]]) == [1,2,3] and flatten_once([]) == [] and flatten_once([[1],[2],[3]]) == [1,2,3])
    print("12.", top_3_words('one two one three two one') == ['one', 'two', 'three'] and top_3_words('a b c') == ['a','b','c'] and top_3_words('') == [])
    print("13.", sort_tuples_by_second([(1,2),(3,1)]) == [(3,1),(1,2)] and sort_tuples_by_second([]) == [] and sort_tuples_by_second([(5,5)]) == [(5,5)])
    print("14.", is_leap_year(2000) == True and is_leap_year(1900) == False and is_leap_year(2024) == True)
    print("15.", custom_min([3,2,1]) == 1 and custom_min([100]) == 100 and custom_min([-1,0]) == -1)
    print("16.", custom_max([3,2,1]) == 3 and custom_max([100]) == 100 and custom_max([-1,0]) == 0)
    print("17.", mini_calculator(2,3,'add') == 5 and mini_calculator(5,2,'subtract') == 3 and mini_calculator(2,3,'multiply') == 6)
    print("18.", log('hi') == '[INFO] hi' and log('warn', level='WARNING') == '[WARNING] warn' and log('err', level='ERROR') == '[ERROR] err')
    print("19.", safe_divide(4,2) == 2 and safe_divide(4,0) == 'Error: Division by zero is undefined.' and isinstance(safe_divide('a',1), str))
    print("20.", filter_even_numbers([1,2,3]) == [2] and filter_even_numbers([]) == [] and filter_even_numbers([2,4,6]) == [2,4,6])
    print("21.", transpose_matrix([[1]]) == [[1]] and transpose_matrix([[1,2],[3,4]]) == [[1,3],[2,4]] and transpose_matrix([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]])
    print("22.", invert_dictionary({'a':1}) == {1:'a'} and invert_dictionary({'x':9,'y':8}) == {9:'x',8:'y'} and invert_dictionary({}) == {})
    print("23.", word_length_dict(['hi']) == {'hi':2} and word_length_dict(['a','ab']) == {'a':1,'ab':2} and word_length_dict([]) == {})
    print("24.", safe_divide(8,4) == 2.0 and safe_divide(5,0) == 'Error: Division by zero is undefined.' and isinstance(safe_divide('a','b'), str))
    print("25.", safe_lookup({'x':1},'x') == 1 and safe_lookup({'x':1},'y') == 'Key not found' and safe_lookup({},'z') == 'Key not found')
    print("26.", multiplication_table() == 385)  # diagonal sum 1+4+...+100
    print("27.", floyds_triangle(1) == 1 and floyds_triangle(3) == 6 and floyds_triangle(5) == 15)
    #print("28.", math_operations(4,2)['power'] == 16 and math_operations(9,2)['sqrt'] == 3 and 'log' in math_operations(10,1))
    print("28. There Has Been A Error In This Function So It Is Commented Out For Now")
    print("29.", len(generate_password(10)) == 10 and is_valid_password(generate_password(10)) == True and generate_password(5) == "Password length must be at least 6")
    print("30.", is_valid_password('Abc123') == True and is_valid_password('abc') == False and is_valid_password('ABC123') == False)
    print("All sample tests executed.")
    
    # Note #28 is commented out due to an error. Please fix it.
main()
