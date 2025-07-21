string1 = "a b c"

list1 = [x if x != " " else "-" for x in string1]

print(list1)