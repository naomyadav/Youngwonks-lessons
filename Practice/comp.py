string1 = "a b c d e f g h i j k l m n o p q r"

list1 = [x if x != " " else "-" for x in string1]

print(list1)