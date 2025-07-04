# Exercise 1 : Print Alphabets
# A
# B C
# D E F
# G H I J
# K L M N O
def alpha_triangle1(num_rows):
    pass

# Exercise 2 : Print A one time B two times …
# A
# B B
# C C C
# D D D D
# E E E E E
def alpha_triangle2(num_rows):
    pass

# Exercise 3 :Write code to print the multiplicaiton table in the following format:
# i = 1 :  1  2  3  4  5  6  7  8  9
# i = 2 :  2  4  6  8 10 12 14 16 18
# i = 3 :  3  6  9 12 15 18 21 24 27
# i = 4 :  4  8 12 16 20 24 28 32 36
# i = 5 :  5 10 15 20 25 30 35 40 45
# i = 6 :  6 12 18 24 30 36 42 48 54
# i = 7 :  7 14 21 28 35 42 49 56 63
# i = 8 :  8 16 24 32 40 48 56 64 72
# i = 9 :  9 18 27 36 45 54 63 72 81
def multiplicaiton_table(num_rows):
    pass

# Exercise 4 :Given a list of lists, find the maximum value in each individual list.
# Example: For [[1, 2], [3, 4, 5], [6]], the output should be:
# 2
# 5
# 6
def max_of_2D_list(list_2D):
    pass

# Exercise 5 :Given a list of lists, find the sum of all elements.
# Example: For [[1, 2], [3, 4], [5, 6]], the sum is 21.
def sum_of_2D_list(list_2D):
    pass



if __name__ == "__main__":
    alpha_triangle1(5)
    alpha_triangle1(10)
    alpha_triangle1(-1)
    alpha_triangle2(5)
    alpha_triangle2(10)
    alpha_triangle2(0)
    multiplicaiton_table(0)
    multiplicaiton_table(5)
    multiplicaiton_table(11)
    list_a = [[1, 2], [3, 4, 5], [6]]
    max_of_2D_list(list_a)
    list_b = [[1, 2], [3, 4], [5, 6]]
    sum_of_2D_list(list_b)
    