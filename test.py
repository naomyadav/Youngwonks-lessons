def find_first_greater(numbers, input_num):
    """
    Finds the first number in a list that is greater than a given input number.

    Args:
        numbers: A list of numbers (integers or floats).
        input_num: The number to compare against.

    Returns:
        The first number greater than input_num, or None if no such number exists.
   
# --- Example Usage ---
my_list = [10, 4, 25, 8, 30, 50]
threshold = 20
result = find_first_greater(my_list, threshold) should return 25. 

# Another example with no matching number
no_match_list = [1, 2, 3, 4]
no_match_threshold = 10
result_no_match = find_first_greater(no_match_list, no_match_threshold) should return None

"""
    for i in numbers:
        if i > input_num:
            return i
        
    
def test_find_first_greater():
    # Test Case 1: Matching number found
    my_list = [10, 4, 25, 8, 30, 50]
    threshold = 20
    assert find_first_greater(my_list, threshold) == 25, "Should return 25"

    # Test Case 2: No matching number
    no_match_list = [1, 2, 3, 4]
    no_match_threshold = 10
    assert find_first_greater(no_match_list, no_match_threshold) is None, "Should return None"

    print("All tests passed!")

# Call the test function
test_find_first_greater()
