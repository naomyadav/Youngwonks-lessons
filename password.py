w = [[],[]]
u=None
p=None
while True:
    u = input("Username:  ")
    p = input("Password:  ")
    if u!="u" and p!="p":
        w[0].append(u)
        w[1].append(p)
    elif u!="u":
        w[0].append(u)
        print("Correct Password")
    elif p!="p":
        w.append(p)
        print("Correct Username")
    else:
        break