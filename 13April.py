# # # # string12121 = input("String:  ")
# # # # number12121 = int(input("Number:  "))
# # # # s1 = list(string12121)#        l
# # # # print(s1[number12121])#        l
# # # # print(s1[-number12121])#       l
# # # # n=0
# # # # for i in range(10):
# # # #     n=n+int(input("Number:  "))
# # # # print(n)
# # # # a_names=[]
# # # # for i in range(10):
# # # #     input_name = input("Name:  ")
# # # #     name_func = """'name'+str(i),"=",input_name"""
# # # #     exec(name_func)
# # # #     if input_name[-1]=="a":
# # # #         a_names.append(input_name)
# # # # print(a_names)
# # # # alpa_list=[chr(ord('a')+i) for i in range(0,26,1)]
# # # # string=input("String:  ")
# # # # if string[1] in alpa_list:
# # # #     string1 = string.upper()
# # # # else:
# # # #     string1 = string.lower()
# # # # print(string1)

# # # for i in range(10):
# # #     print(2+(i*10))
# # list1=[1,2,3,4,5,6,7,8,9,10]
# # num=0
# # for i in range(len(list1)):
# #     if list1[i]%2 == 0:
# #         num = num+list1[i]
# # print(num)

# list1=[1,2,37,152,1379,152,37,2,1]
# dupl1 = []

# for i in range(len(list1)):
#     print(i)
#     lval = list1[i]
#     lplac = i
#     for n in range(i+1,len(list1),1):
#         if list1[n]==lval:
#             dupl1.append(list1[n])

# for t in range(len(dupl1)):
#     list1.remove(dupl1[t])
# print(list1)

phone_number="5152315589"
lucky_number = "1"
pnumber = []
pnl = list(phone_number)

for i in range(len(pnl)):
    if pnl[i] == lucky_number:
        pnumber.append(pnl[i])

phonelen = len(pnumber)
print(phonelen)