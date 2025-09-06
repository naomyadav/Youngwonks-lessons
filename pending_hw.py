


list1 = ["PracticeLvl1.py", "HWJul07.py","HWJul10.py","HWJul13.py","CodingChallenge.py"]
        
        
list2 = ["HW3DJul07.blend","HW3DJul13.blend","HW3DJul22.blend","HW3DAug04.blend","HW3DAug10.blend","HW3DAug17.blend"]
        
list3 = ["HWAug10.py","HWAug17.py"]
        
         
hwlist = [list1, list3]

for hw in hwlist:
    print(hw)
    for hw_name in hw:
        try:
            f=open(hw_name,"w")
            print("Created:"+hw_name)
            f.close()
        except Exception as e:
            print(e)
        

# create fodlers and fiels inisde them as per the above structure

