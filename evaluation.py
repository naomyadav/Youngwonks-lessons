a_names=[]
for i in range(10):
    input_name = input("Name:  ")
    name_func = """'name'+str(i),"=",input_name"""
    exec(name_func)
    print(name1)
    if input_name[-1]=="a":
        a_names.append(input_name)
print(a_names)