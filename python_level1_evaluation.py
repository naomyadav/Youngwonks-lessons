"""
This module contains a collection of function stubs corresponding to
introductory Python programming exercises. Each function header includes
a clear description of the task it is intended to perform. Students are
encouraged to fill in the body of each function to complete the
exercise. None of the functions are implemented; they contain only
``pass`` statements as placeholders.

The exercises cover topics such as type conversion, control flow with
if/elif/else, loops, list manipulation, and basic dictionary operations.
Where appropriate, functions accept parameters instead of reading
interactive input so that they can be reused and tested easily. In
cases where the original prompt describes interactive behavior (such as
asking a user for input), the docstring explains what should happen
inside the function.
"""

from typing import List, Dict, Any


def convert_string_to_int(num_str: str) -> int:
    """Convert a string containing an integer to an actual integer.

    Args:
        num_str: A string representation of an integer (e.g. "42").

    Returns:
        The integer value represented by ``num_str``.

    Example:
        >>> convert_string_to_int("123")
        123

    The student should handle potential errors if the string does not
    represent a valid integer.
    """
    return 0


def reverse_integer(num: int) -> int:
    """Return the integer obtained by reversing the digits of ``num``.

    Args:
        num: An integer whose digits should be reversed (e.g. 1234).

    Returns:
        The integer with its digits in reverse order (e.g. 4321).

    Example:
        >>> reverse_integer(9876)
        6789

    The sign of ``num`` should be preserved; for example, ``-123``
    should become ``-321``.
    """
    return 0


def sum_of_string_numbers(str_list: List[str]) -> int:
    """Sum a list of numeric strings and return the total as an integer.

    Args:
        str_list: A list of strings, each string representing a number
            (e.g. ["1", "2", "3"]).

    Returns:
        The integer sum of the values represented by the strings.

    Example:
        >>> sum_of_string_numbers(["10", "20", "30"])
        60

    The function should convert each string to an integer before
    summing. Handle invalid strings appropriately.
    """
    return 0


def even_or_odd_sum(a: int, b: int) -> str:
    """Determine whether the sum of two integers is even or odd.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        A string "Even sum" if the sum of ``a`` and ``b`` is even,
        otherwise "Odd sum".

    Example:
        >>> even_or_odd_sum(2, 3)
        'Odd sum'
        >>> even_or_odd_sum(4, 4)
        'Even sum'

    The student should implement the logic using an if/else statement.
    """
    return ""


def atm_transaction(balance: float, transaction_type: str, amount: float) -> float:
    """Simulate a simple ATM transaction.

    This function adjusts an account balance based on the transaction
    type and amount. It can simulate either a withdrawal or a deposit.

    Args:
        balance: The current account balance.
        transaction_type: Either "withdraw" or "deposit" (case-insensitive).
        amount: The amount of money to withdraw or deposit.

    Returns:
        The updated account balance after the transaction.

    Raises:
        ValueError: If the transaction type is invalid or if a
        withdrawal amount exceeds the current balance.

    Example:
        >>> atm_transaction(100.0, 'deposit', 50.0)
        150.0
        >>> atm_transaction(100.0, 'withdraw', 20.0)
        80.0
    """
    return 0.0


def average_of_positive_numbers(numbers: List[int]) -> float:
    """Calculate the average of positive numbers until a negative number appears.

    Args:
        numbers: A list of integers. The function should consider
            numbers until a negative number is encountered. Any
            integers after the first negative number should be ignored.

    Returns:
        The average of the positive numbers encountered before the
        first negative number. If no positive numbers are provided
        before a negative value, return ``0.0``.

    Example:
        >>> average_of_positive_numbers([5, 7, 3, -1, 9])
        5.0

    The student should implement this using a while loop or a for loop
    that breaks when a negative number is found.
    """
    return 0.0


def is_prime(n: int) -> bool:
    """Check whether a given positive integer is a prime number.

    Args:
        n: A positive integer to test for primality.

    Returns:
        ``True`` if ``n`` is a prime number, ``False`` otherwise.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False

    By definition, numbers less than 2 are not prime. The student
    should implement an efficient primality test using a loop.
    """
    return False


def number_triangle(height: int) -> List[str]:
    """Generate a triangle pattern of incrementing numbers as a list of strings.

    Args:
        height: The height of the triangle (the number of rows).

    Returns:
        A list of strings, each string representing a row of the
        triangle. For example, height 4 produces
        ['1', '12', '123', '1234'].

    Example:
        >>> number_triangle(3)
        ['1', '12', '123']

    The student should use nested loops to construct each row.
    """
    return []


def primes_in_range(start: int, end: int) -> List[int]:
    """Return a list of prime numbers within a given inclusive range.

    Args:
        start: The beginning of the range (inclusive).
        end: The end of the range (inclusive).

    Returns:
        A list containing all prime numbers ``p`` such that
        ``start <= p <= end``.

    Example:
        >>> primes_in_range(10, 20)
        [11, 13, 17, 19]

    The student should iterate through the range and use the
    ``is_prime`` function to test each number.
    """
    return []


def sum_of_even_numbers(numbers: List[int]) -> int:
    """Sum all even numbers in a list of integers.

    Args:
        numbers: A list of integers.

    Returns:
        The sum of all even integers in the list.

    Example:
        >>> sum_of_even_numbers([1, 2, 3, 4, 5])
        6

    The student should iterate over the list and accumulate the sum of
    values that are divisible by 2.
    """
    return 0


def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Remove duplicate elements from a list while preserving order.

    Args:
        lst: A list containing elements of any hashable type.

    Returns:
        A new list with duplicates removed, preserving the original
        order of first occurrences.

    Example:
        >>> remove_duplicates([1, 2, 2, 3, 1])
        [1, 2, 3]

    The student may use a set to track seen elements.
    """
    return []


def longest_word(words: List[str]) -> str:
    """Return the first word with the maximum length from a list of words.

    Args:
        words: A list of non-empty strings.

    Returns:
        The first word encountered that has the maximum length among
        the words in the list. If the list is empty, return an empty
        string.

    Example:
        >>> longest_word(["apple", "banana", "pear"])
        'banana'

    The student should iterate through the list to find the maximum
    length and its corresponding word.
    """
    return ""


def inventory_system_list(actions: List[Dict[str, Any]]) -> List[str]:
    """Simulate a simple inventory system using a list of strings.

    This function manages an inventory represented as a list of item
    names. It processes a sequence of actions that can add, remove, or
    list items. Each action is a dictionary with a 'type' key and
    optionally an 'item' key when adding or removing.

    Args:
        actions: A list of action dictionaries. Each dictionary has a
            'type' field which can be 'add', 'remove', or 'list'. If
            'type' is 'add' or 'remove', an 'item' field specifies
            which item to add or remove.

    Returns:
        A list representing the inventory after processing all actions.

    Example:
        >>> inventory_system_list([
        ...     {'type': 'add', 'item': 'apple'},
        ...     {'type': 'add', 'item': 'banana'},
        ...     {'type': 'remove', 'item': 'apple'},
        ... ])
        ['banana']

    The student should implement logic to handle each action type and
    update the inventory accordingly. Removing an item that is not
    present should have no effect.
    """
    return []


def square_or_cube_list(numbers: List[int]) -> List[int]:
    """Replace each integer in a list with its square if even or its cube if odd.

    Args:
        numbers: A list of integers.

    Returns:
        A new list where each even number is replaced by its square
        and each odd number is replaced by its cube.

    Example:
        >>> square_or_cube_list([1, 2, 3])
        [1, 4, 27]

    The student should use a loop or list comprehension to perform
    the transformation.
    """
    return []


def cumulative_sum_with_previous(numbers: List[int]) -> List[int]:
    """Replace each element in a list with the sum of itself and the previous element.
    return []
    Args:
        numbers: A list of integers.

    Returns:
        A new list where the first element remains unchanged and each
        subsequent element is replaced by the sum of itself and the
        element before it. For example, the list [1, 2, 3, 4] becomes
        [1, 3, 5, 7].

    Example:
        >>> cumulative_sum_with_previous([10, 20, 30])
        [10, 30, 50]

    The student should iterate through the list and build a new list
    with cumulative sums.
    """
    return []


def delete_key_from_dict(data: Dict[Any, Any], key: Any) -> Dict[Any, Any]:
    """Delete a key-value pair from a dictionary based on the provided key.
    return {}
    Args:
        data: The dictionary from which to delete the key-value pair.
        key: The key to remove.

    Returns:
        A new dictionary with the specified key removed. If the key
        does not exist in the dictionary, return the dictionary
        unchanged.

    Example:
        >>> delete_key_from_dict({'a': 1, 'b': 2}, 'a')
        {'b': 2}

    The student should create a copy of the dictionary to avoid
    mutating the original data structure.
    """
    return {}


def inventory_system_dict(actions: List[Dict[str, Any]]) -> Dict[str, int]:
    """Simulate an inventory system using a dictionary with item quantities.
    return {}
    The inventory is represented as a dictionary mapping item names to
    their quantities. Each action specifies an operation:

    - 'add': Increase the quantity of an item by 1 (or add it to the
      inventory if it does not exist).
    - 'update': Set the quantity of an item to a specific value.
    - 'delete': Remove an item entirely from the inventory.
    - 'list': No operation; can be used to inspect the inventory.

    Args:
        actions: A list of action dictionaries. Each action has a
            'type' key and may include an 'item' key and/or 'quantity'
            key depending on the action type.

    Returns:
        A dictionary representing the inventory after processing all
        actions.

    Example:
        >>> inventory_system_dict([
        ...     {'type': 'add', 'item': 'apple'},
        ...     {'type': 'add', 'item': 'banana'},
        ...     {'type': 'update', 'item': 'banana', 'quantity': 5},
        ...     {'type': 'delete', 'item': 'apple'},
        ... ])
        {'banana': 5}

    The student should implement logic to handle each operation and
    update the dictionary accordingly.
    """
    return {}


def print_students_and_grades(grades: Dict[str, int]) -> List[str]:
    """Return formatted strings of student names and their grades.
    return []
    Args:
        grades: A dictionary mapping student names to integer grades.

    Returns:
        A list of strings, each formatted as "<name>: <grade>" for
        every student in the dictionary.

    Example:
        >>> print_students_and_grades({'Alice': 85, 'Bob': 92})
        ['Alice: 85', 'Bob: 92']

    The student should iterate over the dictionary items and format
    each pair into a string.
    """
    return []


def students_above_grade(grades: Dict[str, int], threshold: int = 90) -> List[str]:
    """Return the names of students whose grades exceed a given threshold.
    return []
    Args:
        grades: A dictionary mapping student names to integer grades.
        threshold: The grade threshold (inclusive) above which a
            student's name should be included.

    Returns:
        A list of student names whose grades are greater than the
        specified threshold.

    Example:
        >>> students_above_grade({'Alice': 88, 'Bob': 95, 'Charlie': 90})
        ['Bob']

    The student should use a loop or list comprehension to filter
    students based on the grade threshold.
    """
    return []


def words_sorted_by_length(words: List[str]) -> List[tuple]:
    """Return a list of (word, length) pairs sorted by word length.
    return []
    Args:
        words: A list of strings.

    Returns:
        A list of tuples where each tuple contains a word and its
        length, sorted in ascending order of length. If two words have
        the same length, their relative order should remain as in the
        original list.

    Example:
        >>> words_sorted_by_length(['sun', 'moon', 'star'])
        [('sun', 3), ('moon', 4), ('star', 4)]

    The student should create the list of pairs then sort it using
    the length as the key.
    """
    return []


def total_salary_expenditure(salaries: Dict[str, float]) -> float:
    """Calculate the total salary expenditure for a company.
    return 0.0
    Args:
        salaries: A dictionary mapping employee names to their salary.

    Returns:
        The sum of all salaries in the dictionary.

    Example:
        >>> total_salary_expenditure({'Alice': 50000.0, 'Bob': 60000.0})
        110000.0

    The student should iterate over the dictionary values and sum
    them.
    """
    return 0.0


def main():
    pass_count = 0
    total_tests = 0

    # convert_string_to_int
    for i, (inp, expected) in enumerate([("123", 123), ("-45", -45), ("0", 0)], 1):
        result = convert_string_to_int(inp)
        if result == expected:
            print(f"convert_string_to_int {i}: PASS")
            pass_count += 1
        else:
            print(f"convert_string_to_int {i}: FAIL")
        total_tests += 1
    print()

    # reverse_integer
    for i, (inp, expected) in enumerate([(9876, 6789), (-123, -321), (100, 1)], 1):
        result = reverse_integer(inp)
        if result == expected:
            print(f"reverse_integer {i}: PASS")
            pass_count += 1
        else:
            print(f"reverse_integer {i}: FAIL")
        total_tests += 1
    print()

    # sum_of_string_numbers
    for i, (inp, expected) in enumerate(([
        (["10", "20", "30"], 60),
        (["1", "2", "3", "4"], 10),
        (["0", "0", "0"], 0)
    ]), 1):
        result = sum_of_string_numbers(inp[0])
        if result == inp[1]:
            print(f"sum_of_string_numbers {i}: PASS")
            pass_count += 1
        else:
            print(f"sum_of_string_numbers {i}: FAIL")
        total_tests += 1
    print()

    # even_or_odd_sum
    for i, (a, b, expected) in enumerate([(2, 3, 'Odd sum'), (4, 4, 'Even sum'), (0, 1, 'Odd sum')], 1):
        result = even_or_odd_sum(a, b)
        if result == expected:
            print(f"even_or_odd_sum {i}: PASS")
            pass_count += 1
        else:
            print(f"even_or_odd_sum {i}: FAIL")
        total_tests += 1
    print()

    # atm_transaction
    for i, (bal, typ, amt, expected) in enumerate([
        (100.0, 'deposit', 50.0, 150.0),
        (100.0, 'withdraw', 20.0, 80.0),
        (0.0, 'deposit', 100.0, 100.0)
    ], 1):
        result = atm_transaction(bal, typ, amt)
        if result == expected:
            print(f"atm_transaction {typ} {i}: PASS")
            pass_count += 1
        else:
            print(f"atm_transaction {typ} {i}: FAIL")
        total_tests += 1
    print()

    # average_of_positive_numbers
    for i, (inp, expected) in enumerate([
        ([5, 7, 3, -1, 9], 5.0),
        ([10, 20, -5, 30], 15.0),
        ([-1, 5, 6], 0.0)
    ], 1):
        result = average_of_positive_numbers(inp)
        if result == expected:
            print(f"average_of_positive_numbers {i}: PASS")
            pass_count += 1
        else:
            print(f"average_of_positive_numbers {i}: FAIL")
        total_tests += 1
    print()

    # is_prime
    for i, (inp, expected) in enumerate([(7, True), (10, False), (2, True)], 1):
        result = is_prime(inp)
        if result == expected:
            print(f"is_prime {i}: PASS")
            pass_count += 1
        else:
            print(f"is_prime {i}: FAIL")
        total_tests += 1
    print()

    # number_triangle
    for i, (inp, expected) in enumerate([
        (3, ['1', '12', '123']),
        (1, ['1']),
        (0, [])
    ], 1):
        result = number_triangle(inp)
        if result == expected:
            print(f"number_triangle {i}: PASS")
            pass_count += 1
        else:
            print(f"number_triangle {i}: FAIL")
        total_tests += 1
    print()

    # primes_in_range
    for i, (start, end, expected) in enumerate([
        (10, 20, [11, 13, 17, 19]),
        (2, 5, [2, 3, 5]),
        (14, 16, [])
    ], 1):
        result = primes_in_range(start, end)
        if result == expected:
            print(f"primes_in_range {i}: PASS")
            pass_count += 1
        else:
            print(f"primes_in_range {i}: FAIL")
        total_tests += 1
    print()

    # sum_of_even_numbers
    for i, (inp, expected) in enumerate([
        ([1, 2, 3, 4, 5], 6),
        ([2, 4, 6], 12),
        ([1, 3, 5], 0)
    ], 1):
        result = sum_of_even_numbers(inp)
        if result == expected:
            print(f"sum_of_even_numbers {i}: PASS")
            pass_count += 1
        else:
            print(f"sum_of_even_numbers {i}: FAIL")
        total_tests += 1
    print()

    # remove_duplicates
    for i, (inp, expected) in enumerate([
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        (['a', 'b', 'a', 'c'], ['a', 'b', 'c']),
        ([], [])
    ], 1):
        result = remove_duplicates(inp)
        if result == expected:
            print(f"remove_duplicates {i}: PASS")
            pass_count += 1
        else:
            print(f"remove_duplicates {i}: FAIL")
        total_tests += 1
    print()

    # longest_word
    for i, (inp, expected) in enumerate([
        (["apple", "banana", "pear"], "banana"),
        (["hi", "hello", "hey"], "hello"),
        ([], "")
    ], 1):
        result = longest_word(inp)
        if result == expected:
            print(f"longest_word {i}: PASS")
            pass_count += 1
        else:
            print(f"longest_word {i}: FAIL")
        total_tests += 1
    print()

    # inventory_system_list
    for i, (inp, expected) in enumerate([
        ([{'type': 'add', 'item': 'apple'}, {'type': 'add', 'item': 'banana'}, {'type': 'remove', 'item': 'apple'}], ['banana']),
        ([{'type': 'add', 'item': 'apple'}, {'type': 'add', 'item': 'apple'}, {'type': 'remove', 'item': 'banana'}], ['apple', 'apple']),
        ([], [])
    ], 1):
        result = inventory_system_list(inp)
        if result == expected:
            print(f"inventory_system_list {i}: PASS")
            pass_count += 1
        else:
            print(f"inventory_system_list {i}: FAIL")
        total_tests += 1
    print()

    # square_or_cube_list
    for i, (inp, expected) in enumerate([
        ([1, 2, 3], [1, 4, 27]),
        ([2, 4, 6], [4, 16, 36]),
        ([1, 3, 5], [1, 27, 125])
    ], 1):
        result = square_or_cube_list(inp)
        if result == expected:
            print(f"square_or_cube_list {i}: PASS")
            pass_count += 1
        else:
            print(f"square_or_cube_list {i}: FAIL")
        total_tests += 1
    print()

    # cumulative_sum_with_previous
    for i, (inp, expected) in enumerate([
        ([10, 20, 30], [10, 30, 50]),
        ([1, 2, 3, 4], [1, 3, 5, 7]),
        ([5], [5])
    ], 1):
        result = cumulative_sum_with_previous(inp)
        if result == expected:
            print(f"cumulative_sum_with_previous {i}: PASS")
            pass_count += 1
        else:
            print(f"cumulative_sum_with_previous {i}: FAIL")
        total_tests += 1
    print()

    # delete_key_from_dict
    for i, (inp, key, expected) in enumerate([
        ({'a': 1, 'b': 2}, 'a', {'b': 2}),
        ({'x': 10, 'y': 20}, 'z', {'x': 10, 'y': 20}),
        ({}, 'a', {})
    ], 1):
        result = delete_key_from_dict(inp, key)
        if result == expected:
            print(f"delete_key_from_dict {i}: PASS")
            pass_count += 1
        else:
            print(f"delete_key_from_dict {i}: FAIL")
        total_tests += 1
    print()

    # inventory_system_dict
    for i, (inp, expected) in enumerate([
        ([{'type': 'add', 'item': 'apple'}, {'type': 'add', 'item': 'banana'}, {'type': 'update', 'item': 'banana', 'quantity': 5}, {'type': 'delete', 'item': 'apple'}], {'banana': 5}),
        ([{'type': 'add', 'item': 'apple'}, {'type': 'add', 'item': 'apple'}, {'type': 'update', 'item': 'apple', 'quantity': 3}], {'apple': 3}),
        ([], {})
    ], 1):
        result = inventory_system_dict(inp)
        if result == expected:
            print(f"inventory_system_dict {i}: PASS")
            pass_count += 1
        else:
            print(f"inventory_system_dict {i}: FAIL")
        total_tests += 1
    print()

    # print_students_and_grades
    for i, (inp, expected) in enumerate([
        ({'Alice': 85, 'Bob': 92}, ['Alice: 85', 'Bob: 92']),
        ({'Tom': 70}, ['Tom: 70']),
        ({}, [])
    ], 1):
        result = print_students_and_grades(inp)
        if result == expected:
            print(f"print_students_and_grades {i}: PASS")
            pass_count += 1
        else:
            print(f"print_students_and_grades {i}: FAIL")
        total_tests += 1
    print()

    # students_above_grade
    for i, (inp, expected) in enumerate([
        ({'Alice': 88, 'Bob': 95, 'Charlie': 90}, ['Bob']),
        ({'A': 91, 'B': 89}, ['A']),
        ({'A': 80, 'B': 85}, [])
    ], 1):
        result = students_above_grade(inp)
        if result == expected:
            print(f"students_above_grade {i}: PASS")
            pass_count += 1
        else:
            print(f"students_above_grade {i}: FAIL")
        total_tests += 1
    print()

    # words_sorted_by_length
    for i, (inp, expected) in enumerate([
        (['sun', 'moon', 'star'], [('sun', 3), ('moon', 4), ('star', 4)]),
        (['a', 'ab', 'abc'], [('a', 1), ('ab', 2), ('abc', 3)]),
        ([], [])
    ], 1):
        result = words_sorted_by_length(inp)
        if result == expected:
            print(f"words_sorted_by_length {i}: PASS")
            pass_count += 1
        else:
            print(f"words_sorted_by_length {i}: FAIL")
        total_tests += 1
    print()

    # total_salary_expenditure
    for i, (inp, expected) in enumerate([
        ({'Alice': 50000.0, 'Bob': 60000.0}, 110000.0),
        ({'A': 0.0, 'B': 0.0}, 0.0),
        ({}, 0.0)
    ], 1):
        result = total_salary_expenditure(inp)
        if result == expected:
            print(f"total_salary_expenditure {i}: PASS")
            pass_count += 1
        else:
            print(f"total_salary_expenditure {i}: FAIL")
        total_tests += 1
    print()

    print(f"Total passed: {pass_count} out of {total_tests} test cases.")

if __name__ == "__main__":
    main()
